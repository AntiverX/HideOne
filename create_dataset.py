from os import listdir
from os.path import isfile, join
from shutil import move
import os

onlyfiles = [f for f in listdir("/root/dataset_50000") if isfile(join("/root/dataset_50000", f))]
val = []
train = []
for i in range(len(onlyfiles)):
    if i < 5000:
        val.append(join("/root/dataset_50000", onlyfiles[i]))
    else:
        train.append(join("/root/dataset_50000", onlyfiles[i]))

try:
    os.mkdir("/root/dataset_50000/val")
    os.mkdir("/root/dataset_50000/train")
except:
    pass

for file in train:
    move(file, os.path.join("/root/dataset_50000/train", os.path.split(file)[1]))
for file in val:
    move(file, os.path.join("/root/dataset_50000/val", os.path.split(file)[1]))