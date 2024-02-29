import numpy as np
'''
Loader functions for different type of image files
- JPEG : load_jpeg
- RAF: load_raf
- RAW: load_raw
'''

def load_jpeg(path):
    '''
    JPEG
    https://github.com/corkami/formats/blob/master/image/jpeg.md#

    returns numpy array with H, W, C
    ''' 
    import cv2 as cv
    return cv.imread(cv.samples.findFile(path)).astype(np.uint8)


def load_raf(path):
    '''
    https://github.com/LibRaw/LibRaw
    '''
    import rawpy
    return rawpy.imread(path).raw_image


def file_type(path):
    '''
    Determine what type of img is it JPEG, RAW, ... 
    or if it isnt an image
    '''
    pass