pip install gdown
gdown https://drive.google.com/uc?id=1_aMwuZXYO8rYiBHKxxuuSjF4Mb-A3Fyr
mkdir dataset_50000 dataset_50000/train dataset_50000/val
tar -xvf ILSVRC2012_img_val_50000.tar -C dataset_50000

apt install git screen -y
git clone https://github.com/AntiverX/HideOne.git
cd /root/HideOne
python create_dataset.py
pip install -r requirements.txt