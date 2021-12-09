from os import listdir
from os.path import isfile, join
from shutil import move
import os
from sklearn.model_selection import ShuffleSplit
import numpy as np

PATH = "/home/lab/ILSVRC2012_img_val_50000"
VAL = "/home/lab/dataset/val"
TRAIN = "/home/lab/dataset/train"

onlyfiles = [os.path.join(PATH, f) for f in listdir(PATH) if isfile(join(PATH, f))]
data = np.array(onlyfiles)

rs = ShuffleSplit(n_splits=1, test_size=0.1, random_state=0)
for train_index, test_index in rs.split(data):
    train = data[train_index]
    val = data[test_index]
    for file in train:
        move(file, os.path.join(TRAIN, os.path.split(file)[1]))
    for file in val:
        move(file, os.path.join(VAL, os.path.split(file)[1]))