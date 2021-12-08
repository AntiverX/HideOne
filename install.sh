pip install gdown
gdown https://drive.google.com/uc?id=1_aMwuZXYO8rYiBHKxxuuSjF4Mb-A3Fyr
pip install -r requirements.txt
mkdir dataset_50000 dataset_50000/train dataset_50000/val
tar -xvf ILSVRC2012_img_val_50000.tar -C dataset_50000
cd ./torch_test
python create_dataset.py
