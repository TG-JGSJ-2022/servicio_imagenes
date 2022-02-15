# Libraries needed
from math import ceil, floor
import cv2
import numpy as np

def image_resize_average_color(image, width = 299, height = 299, inter = cv2.INTER_AREA):
    #-------------------------------------------------
    #                 Resize image
    #-------------------------------------------------
    # Initialize the dimensions of the image to be resized and grab the image size
    dim = None
    h, w, _ = image.shape

    # Calculate the ratio of the width and construct the dimensions
    r = height / float(w) if w > h else height / float(h)
    dim = (width, int(h * r)) if w > h else (int(w * r), height)

    # Resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    #-------------------------------------------------
    #            Calculate average color
    #-------------------------------------------------
    h, w, _ = resized.shape
    average_color = [0, 0, 0]
    average = h * w

    # Traverse image
    for i in range(0, h):
        for j in range(0, w):
            pixel = image[i][j]
            average_color[0] += pixel[0]
            average_color[1] += pixel[1]
            average_color[2] += pixel[2]
        # Eof
    # Eof

    average_color = list(map(lambda i : i / average, average_color))

    #-------------------------------------------------
    #  Calculate padding to add to the resized image
    #-------------------------------------------------
    # Top and bottom border
    top = ceil((299 - h) / 2) if h < 299 else 0
    bottom = floor((299 - h) / 2) if h < 299 else 0
    # Left and right border
    left = abs(ceil((299 - w) / 2)) if w < 299 else 0
    right = abs(floor((299 - w) / 2)) if w < 299 else 0

    image_with_padding = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=average_color)
    
    #-------------------------------------------------
    #      Return resized image with padding 
    #-------------------------------------------------
    return image_with_padding
# Eod

def image_resize_dominant_color(image, width = 299, height = 299, inter = cv2.INTER_AREA):
    
    # Initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    h, w, c = image.shape

    # Calculate the ratio of the width and construct the
    # dimensions
    r = width / float(w)
    dim = (width, int(h * r))

    # Resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # Calculate dominant color of the image
    data = np.reshape(resized, (-1,3))
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    _, _, centers = cv2.kmeans(data,1,None,criteria,10,flags)

    dominant = centers[0].astype(np.int32)
    dominant_color = [ int(i) for i in dominant ]

    # Add padding to the image
    h, w, _ = resized.shape

    #-------------------------------------------------
    #        Calculate padding to add to image
    #-------------------------------------------------
    # Top and bottom border
    top = abs(ceil((299 - h) / 2)) if h != 299 else 0
    bottom = abs(floor((299 - h) / 2)) if h != 299 else 0
    # Left and right border
    left = abs(ceil((299 - w) / 2)) if w != 299 else 0
    right = abs(floor((299 - w) / 2)) if w != 299 else 0

    image_with_padding = cv2.copyMakeBorder(resized, top, bottom, left, right, cv2.BORDER_CONSTANT, value=dominant_color)
    
    # return the resized image with padding
    return image_with_padding
# Eod

# ------------------------------------
# TEST 
# ------------------------------------

# Read the image using imread function
# image = cv2.imread('./image.jpg')
# print("Original image shape : ", image.shape)

# resized_image_average = image_resize_average_color(image, 299, 299)
# print("Resized image shape (AVERAGE) : ", resized_image_average.shape)

# resized_image_dominant = image_resize_average_color(image, 299, 299)
# print("Resized image shape (DOMINANT) : ", resized_image_dominant.shape)

# cv2.imshow("AVERAGE", resized_image_average)
# cv2.imshow("DOMINANT", resized_image_dominant)
# cv2.waitKey()