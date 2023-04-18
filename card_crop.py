from PIL import Image
import os

img = Image.open(os.path.abspath('sprites/cards.png'))
mast, card = ['C', 'B', 'K', 'P'], ['T', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
width, height = img.size
width //= 2.25
height *= 2.25

for i in range(4):
    for j in range(13):
        im_crop = img.crop((10+height*j//13, width*i//4, 10+height*(j+1)//13, width*(i+1)//4))
        im_crop.save(os.path.abspath('sprites/' + mast[i] + card[j] + '.png'))