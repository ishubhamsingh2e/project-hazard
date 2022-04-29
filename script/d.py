import cv2
import numpy as np
import os
from PIL import Image

path = "data/fullpage"
data = os.listdir(path=path)
file = f"{path}/{data[0]}"

for i in data:
    im = Image.open(f"{path}/{i}")
    im = im.crop((134, 111, 1144, 1539))
    im.save(f'out/{i}')