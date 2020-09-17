import cv2
import numpy as np

# Hough Transformation algorithm
# 1) Edge detection(using Canny edge detector)
# 2) Maping of edge points to the hough space and storage in an accumulator
# 3) Interpretation of the accumulator to yield lines of infinte length. The interpretation is done by thresholding.
# 4) Conversion of infinite lines to finite lines
# There are 2 types of Hough Line Transformations in OpenCV:-
# a) Standard Hough Transform(Hough Lines method)
# b) Probabilistic Hough Line Transform(Hough LinesP mathod)

img = cv2.imread('sudoku.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)
# cv2.HoughLines(image, rho value(normally it is taken as 1), 
# theta vlaue(resolution of accumulator in radians), accumulator_threshold)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    
    # x1 stores the rounded of value of (rho * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded of value of (rho * sin(theta) + 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded of value of (rho * cos(theta) + 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded of value of (rho * sin(theta) - 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
