import cv2
import numpy as np
import os
from PIL import Image

path = "data/original"
data = os.listdir(path=path)
flg = 1

for i in data:
    os.rename(f"{path}/{i}", f"{path}/{flg}.jpg")
    flg += 1