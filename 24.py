import cv2
import numpy as np

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
# cv2.findContours(threshold(thresh), contour mode, contour approximation method)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# contours is a python list of all the contours in the image.
# hierarchy is the optional output vector which contains information about image topology
print("Number of contours: " + str(len(contours)))
print(contours[0])

# to join all the coordinates of all the contours we use the following method
# cv2.drawContours(original image, contours, contours indexes(-1: finds all contours), colour, thickness)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()
