import cv2
import numpy as np
import os
from PIL import Image

path = "data0"
data = os.listdir(path=path)
file = f"{path}/{data[0]}"

for i in data:
    print(i)
    im = Image.open(f"{path}/{i}")
    width, height = im.size
    hg = int(height/3)
    im0 = im.crop((0, 0, width, hg))
    im1 = im.crop((0, hg, width, hg*2))
    im2 = im.crop((0, hg*2, width, hg*3))
    im0.save(f'out1/_0{i}')
    im1.save(f'out1/_1{i}')
    im2.save(f'out1/_2{i}') 