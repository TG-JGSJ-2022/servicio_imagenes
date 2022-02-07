# Libraries needed
from math import ceil, floor
import cv2
import numpy as np

def image_resize(image, width = 299, height = 299, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    h, w, c = image.shape

    # calculate the ratio of the width and construct the
    # dimensions
    r = width / float(w)
    dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # Calculate dominant color of the image
    data = np.reshape(resized, (-1,3))
    print(data.shape)
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness,labels,centers = cv2.kmeans(data,1,None,criteria,10,flags)

    dominant = centers[0].astype(np.int32)
    dominant_color = [ int(i) for i in dominant ]

    # Add padding to the image
    h, w, _ = resized.shape

    #-------------------------------------------------
    #        Calculate padding to add to image
    #-------------------------------------------------
    # Top and bottom border
    top = ceil((299 - h) / 2) if h != 299 else 0
    bottom = floor((299 - h) / 2) if h != 299 else 0
    # Left and right border
    left = ceil((299 - w) / 2) if w != 299 else 0
    right = floor((299 - w) / 2) if w != 299 else 0

    image_with_padding = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=dominant_color)
    
    # return the resized image with padding
    return image_with_padding
# Eod

# TEST 
# Read the image using imread function
# image = cv2.imread('image.png')
# print(image.shape)

# resized_image = image_resize(image, 299, 299)

# cv2.imshow("padding.png", resized_image)
# cv2.waitKey()