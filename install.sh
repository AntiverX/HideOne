pip install gdown
gdown https://drive.google.com/uc?id=1_aMwuZXYO8rYiBHKxxuuSjF4Mb-A3Fyr
gdown 'https://drive.google.com/uc?id=1-Qlf1DSAIDnXV1sXy-_Jjudk4l9ThrjU'

mkdir /home/lab/dataset /home/lab/dataset/train /home/lab/dataset/val
tar -xvf ILSVRC2012_img_val_50000.tar -C ILSVRC2012_img_val_50000

apt install git screen unrar -y
git clone https://github.com/AntiverX/HideOne.git
cd /root/HideOne
python create_dataset.py
pip install -r requirements.txt


# 设置自动上传
gdown 'https://drive.google.com/uc?id=1Q5WjPSLvUpmbpwH-dg9eQkP3_H5X2XZB'
chmod +x gdrive
./gdrive list



# tar -zcvf valset.tar.gz 'f606987b3fbe_2021-12-10-04_01_21 '$'\347\273\247\347\273\255\351\231\215\344\275\216\357\274\214\346\225\210\346\236\234\346\233\264\345\245\275'
# ./gdrive upload valset.tar.gz