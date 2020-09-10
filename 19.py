import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# kernel = 1 / 25 * ((5, 5)matrix)
kernel = np.ones((5, 5), np.float32)/25

#cv2.filter2D(image, desired depth of the destination image, kernel)
# filter2D is used for homogeneous filter algortihm
dst = cv2.filter2D(img, -1, kernel)

#cv2.blur(image, kernel)
blur = cv2.blur(img, (5, 5))

# gaussian filter algorithm : gaussian filter is nothin but using different
# weight kernel, in both x and y direction, i.e. pixels located on the center
# have higher weight and pixels located on the side have lower weight
#cv2.GaussianBlur(image, kernel, sigmaX value)
gblur = cv2.GaussianBlur(img, (5, 5), 0)

# cv2.medianBlur(img, kernel(the kernel size should be odd here))
median = cv2.medianBlur(img, 5)

#cv2.bilateraFilter(image, diamter of each pixel and its neighbourbood, sigma colour, sigma space)
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateral']
images = [img, dst, blur, gblur, median, bilateral]

for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    
plt.show()
