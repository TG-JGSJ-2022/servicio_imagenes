import base64
from pickletools import uint8
import numpy as np
import cv2 

def imageb64_to_CV2(image64):
    imageB=base64.b64encode(image64)
    imageR=np.frombuffer(imageB,dtype=np.uint8)
    imageCV=cv2.imdecode(imageR,flags=cv2.IMREAD_COLOR)
    return imageCV
