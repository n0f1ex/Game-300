from PIL import Image
import os

img = Image.open(os.path.abspath('sprites/masti.png'))
mast = ['P', 'C', 'B', 'K']
width, height = img.size
width = 600
height = 600

for i in range(2):
    for j in range(2):
        im_crop = img.crop((i * height, j * width, i * height + height, j * width + width))
        im_crop.save(os.path.abspath('sprites/' + mast[i + j * 2] + '.png'))