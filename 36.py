# 1) Determine which windows produce very large variations in intensity
# when moved in both x and y directions.
# 2) With each such window found, a score R is computed.
# 3) After applying a threshold to this score, important corners are 
# selected and marked.
import cv2
import numpy as np

img = cv2.imread('right01.jpg')

cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
# cv2.cornerHarris(image, block_size, ksize, 'k' harris detector free parameter)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

dst = cv2.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
