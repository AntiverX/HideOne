pip install gdown
gdown https://drive.google.com/uc?id=1_aMwuZXYO8rYiBHKxxuuSjF4Mb-A3Fyr
gdown 'https://drive.google.com/uc?id=1-Qlf1DSAIDnXV1sXy-_Jjudk4l9ThrjU'

mkdir dataset_50000 /root/dataset_50000/train dataset_50000/val
tar -xvf ILSVRC2012_img_val_50000.tar -C dataset_50000
unrar e collections.rar /root/dataset_50000/train

apt install git screen unrar -y
git clone https://github.com/AntiverX/HideOne.git
cd /root/HideOne
python create_dataset.py
pip install -r requirements.txt


# 设置自动上传
gdown 'https://drive.google.com/uc?id=1Q5WjPSLvUpmbpwH-dg9eQkP3_H5X2XZB'
chmod +x gdrive
./gdrive list



# tar -zcvf archive-name.tar.gz
# gdrive upload archive-name.tar.gz