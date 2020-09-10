import numpy as np
import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
# cv2.dilate(image, kernel(a kernel is some type of shape that we want to apply on the image),
# iterations(no. of times we want to perform dilation on our image))
dilation = cv2.dilate(mask, kernel, iterations = 2)

# cv2.erode(image, kernel, iterations)
erosion = cv2.erode(mask, kernel, iterations = 1)

#cv2.morphologyEx(image, type of morphological operation we want to perform, kernel)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)


titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, 1 + i), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
