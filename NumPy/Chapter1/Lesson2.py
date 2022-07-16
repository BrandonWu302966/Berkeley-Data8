#using numpy functions and array operations to invert an image

import numpy as np
import math
import random
from IPython.display import display
from PIL import Image

im = Image.open("kid.png")
array = np.array(im)

def shape():
    print(array.shape)
    print(array)

def mask():
    mask = np.full(array.shape, 255)
    print(mask)

def invert():
    mask = np.full(array.shape, 255)
    modified_array = array - mask
    modified_array = modified_array * -1
    modified_array = modified_array.astype(np.uint8)
    print(modified_array)
    new_im = Image.fromarray(modified_array)
    new_im.save('inverted_image.png')


invert()