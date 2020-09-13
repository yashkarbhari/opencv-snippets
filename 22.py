import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("lena.jpg")

# cv2.pyrDown(image)
lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

#cv2.pyrUp(img)
hr2 = cv2.pyrUp(lr2)

cv2.imshow("Original Image", img)
cv2.imshow("pyrdown 1 image", lr1)
cv2.imshow('pyrdown 2 image', lr2)
cv2.imshow('pyrup', hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()

-----------------------------------------------------------------
# A more dynamic approach

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg')
layer = img.copy()
gp = [layer]

for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i), layer)
    
cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
