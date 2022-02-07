import base64
from pickletools import uint8
import numpy as np

import cv2 

def imageb64_to_CV2(image64):
    encoded_data = image64.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("imagen.png",img)
    return img
