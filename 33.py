# First, a classifier is trained with a few hundred sample views of a 
# particular object(i.e., a face or a car), called positive examples,
# that are scaled to the same size, and negative examples- arbitary 
# images of the same size.

import cv2
import numpy as np

# cv2.CascadeClassifier(trained classifier file name)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.CascadeClassifier.detectMultiScale(image, scaleFactor, minNeighbors)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey()
