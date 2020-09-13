import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', 0)
cv2.namedWindow('image')

# Canny edge detection in 5 steps:
# 1) Noise reduction(smootheness the image)
# 2) Gradient calculation(finds intensity of the image)
# 3) Non-maximum suppresion(to get rid of spurious response)
# 4) Double Threshold(to determine potential edges)
# 5) Edge Tracking by Hysteresis(track edges by hysteresis)
def nothing(x):
    print(x)

cv2.createTrackbar('th1', 'image', 0, 300, nothing)
cv2.createTrackbar('th2', 'image', 0, 300, nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    
    th1 = cv2.getTrackbarPos("th1", "image")
    th2 = cv2.getTrackbarPos("th2", "image")

#cv2.Canny(image, threshold1, threshold2)
    canny = cv2.Canny(img, th1, th2)
    cv2.imshow('canny', canny)
    
    if k == 27:
        break
    

# titles = ['image', 'canny']
# images = [img, canny]
# for i in range(2):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#     plt.figure(figsize = (20, 10))
# plt.show()

cv2.destroyAllWindows()
