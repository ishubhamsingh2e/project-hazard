import cv2
import numpy as np
import os
from PIL import Image

path = "data/card/red"
data = os.listdir(path=path)
# data.remove("red")
flg = 1

for i in data:
    os.rename(f"{path}/{i}", f"new/{flg}.jpg")
    flg += 1