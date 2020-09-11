import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

#cv2.Laplacian(image, data_type, ksize(kernel_size(optional)))
lap = cv2.Laplacian(img, cv2.CV_64F, ksize = 1)
lap = np.uint8(np.absolute(lap))

#cv2.Sobel(image, data_type, dx(order of derivative x), dy(order of derivative y))
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# to combine both sobelX, and sobelY
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    plt.figure(figsize = (20, 10))
    
plt.show()
