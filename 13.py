import cv2
import numpy as np

# makes a black image
img1 = np.zeros((794, 600, 3), np.uint8)
#print(img1.shape)
# makes a white rectangle applies it to the 1st image
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2= cv2.imread("opencv-logo.png")

#bitwise_and(img that we want to show a particular part, the mask)
bitAnd = cv2.bitwise_and(img2, img1)

#bitwise_Or(the mask, img that we want to show a particular part)
bitOr =cv2.bitwise_or(img2, img1)


bitXor = cv2.bitwise_xor(img2, img1)

# In bitwise_not() when we give the image, the not operator changes 
#the colour of the image  to the opposite of the image.
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXor", bitXor)
cv2.imshow("bitNot1", bitNot1)
cv2.imshow("bitNot2", bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()
