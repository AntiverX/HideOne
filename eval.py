from PIL import Image
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.utils.data
from torchvision import transforms
from models.HidingUNet import UnetGenerator
from models.RevealNet import RevealNet
import torch.nn.functional as F
from util import AverageMeter, pad_to, unpad
from torchvision.utils import save_image


def get_target_model(input_image):
    model = torch.hub.load('pytorch/vision:v0.10.0', 'vgg11', pretrained=True, skip_validation=True).cuda()
    model.eval()
    url, filename = ("https://github.com/pytorch/hub/raw/master/images/dog.jpg", "dog.jpg")

    with torch.no_grad():
        output = model(input_image.cuda())

    # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    with open("eval/imagenet_classes.txt", "r") as f:
        categories = [s.strip() for s in f.readlines()]
    # Show top categories per image
    top5_prob, top5_catid = torch.topk(probabilities, 1)
    for i in range(top5_prob.size(0)):
        print(categories[top5_catid[i]], top5_prob[i].item())

def test_trojan():
    # arguments
    HnetPath = "netH_epoch_34,sumloss=0.014938,Hloss=0.000482.pth"
    RnetPath = "netR_epoch_34,sumloss=0.014938,Rloss=0.019275.pth"

    Hnet = UnetGenerator(input_nc=6, output_nc=3, num_downs=5, output_function=nn.Sigmoid)
    Hnet.cuda()
    Hnet.load_state_dict(torch.load(HnetPath))

    Rnet = RevealNet(output_function=nn.Sigmoid)
    Rnet.cuda()
    Rnet.load_state_dict(torch.load(RnetPath))

    Hnet.eval()
    Rnet.eval()
    Hnet.zero_grad()
    Rnet.zero_grad()

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])

    # # dog image
    # input_image = Image.open("dog.jpg")
    # input_tensor = preprocess(input_image)
    # cover_batch = input_tensor.unsqueeze(0)
    # print(get_target_model(cover_batch))
    # exit()

    # cover image
    input_image = Image.open("eval/cover.JPEG")
    input_tensor = preprocess(input_image)
    cover_batch = input_tensor.unsqueeze(0)
    cover_batch, pads = pad_to(cover_batch, 256)

    # secret image
    input_image = Image.open("eval/dog.jpg")
    input_tensor = preprocess(input_image)
    secret_batch = input_tensor.unsqueeze(0)
    secret_batch, _ = pad_to(secret_batch, 256)

    # concate
    concat_img = torch.cat([cover_batch, secret_batch], dim=1)

    with torch.no_grad():
        container_img = Hnet(concat_img.cuda())  # take concat_img as input of H-net and get the container_img

        # 256 to 224
        container_img_unpad = unpad(container_img, pads)
        # 224 to 256
        container_img_repad, _ = pad_to(container_img_unpad, 256)

        #
        rev_secret_img = Rnet(container_img_repad.cuda())  # containerImg as input of R-net and get "rev_secret_img"
        rev_secret_img_unpad = unpad(rev_secret_img, pads)

    save_image(container_img[0], "container256.jpg")
    save_image(rev_secret_img[0], "recovered256.jpg")
    save_image(container_img_unpad[0], "container.jpg")
    save_image(rev_secret_img_unpad[0], "recovered.jpg")
    # get_target_model(secret_batch)
    # get_target_model(rev_secret_img_unpad)

if __name__ == "__main__":
    test_trojan()
