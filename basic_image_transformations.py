import numpy as np

'''
Basic Image Transformations
- Brightness
- Contrast
...

'''

def brightness(img, value):
    '''
    Modifies image brightness
    value > 0 increases brightness, 
          < 0 decreases brightness 
          ( 0 stays the same )
    '''
    return img + value


def contrast(img, value):
    '''
    Modify Image contrast
    value > 1 increases contrast, 
          < 1 decreases contrast. 
          ( 1 does nothing )
    '''
#     return (img).astype(np.uint8) * value # if value != 1 else img
    factor = value
    return np.clip(factor*(img.astype(np.int16)-128)+128, 0, 255)


def resize(img, new_res):
    '''
    Resize img with H, W to 
    new_res (H', W') spatial resolution
    '''
    pass