from PIL import Image, ImageFilter
import numpy
import random
import queue as queue
from thresholding import thresholding
from segmentation import Segments, Region
import os.path
name = 'garden.jpg'
file_name = name[:name.index('.')] + '_regions.txt'
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

if not os.path.isfile(file_name):
    thresholding(name)
    Segments(name, file_name)

f = open(file_name, 'r')
all_regions = f.read()
all_regions = all_regions.split('checkpoint')[:-1]
for i in range(len(all_regions)):
    all_regions[i] = all_regions[i].split(' ')[:-1]

im = Image.open(name)
pix = im.load()
n = 1
for i in range(len(all_regions)):
    randcolor = (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))
    selected_region = all_regions[i]
    for j in range(len(selected_region)//2):
        x = int(selected_region[2*j])
        y = int(selected_region[2*j + 1])
        pix[x, y] = randcolor
    print('Region', n, 'is painted.')
    n += 1

im.save('colorized_' + name, 'PNG')
print('Done!')