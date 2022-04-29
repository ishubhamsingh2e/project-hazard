import cv2
import numpy as np
import os
from PIL import Image

path = "out"
data = os.listdir(path=path)
file = f"{path}/{data[0]}"

for i in data:
    print(i)
    im = Image.open(f"{path}/{i}")
    width, height = im.size
    wd = int(width/3)
    im0 = im.crop((0, 0, wd, height))
    im1 = im.crop((wd, 0, wd*2, height))
    im2 = im.crop((wd*2, 0, wd*3, height))
    im0.save(f'wd/_0{i}')
    im1.save(f'wd/_1{i}')
    im2.save(f'wd/_2{i}')