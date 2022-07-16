import numpy as np
from PIL import Image
import math

def invert(a):
    while True:
        try:
            im = Image.open(a)
        except:
            print("invalid")
            break
        else:
            array = np.array(im)
            if int(array.shape[2]) >= 4:
                print(array.shape)
                print("Too many rgb colors")
            mask = np.full(array.shape, 255)
            modified_array = array - mask
            modified_array = modified_array * -1
            modified_array = modified_array.astype(np.uint8)
            new_im = Image.fromarray(modified_array)
            new_im.save('inverted_image.png')
            break

invert('images.jpeg')