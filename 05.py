import cv2

img = cv2.imread('lena.jpg', 1)

# line(image you want to load, pt 1, pt 2, (B, G, R), thickness)
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 5)

# arrowdLine() makes a arrowed line
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)

# rectangle(image, pt 1(left-top vertex), pt 2(right bottom vertex), thickness)
# to fill everything inside the rectangle use thickness as -1
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

# circle(image, center, radius, color, thickness)
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)

# putText(image, 'what text you want to put in the images', coordinates from where 
# do you want to start the text, font, font size, color of the font, thickness, line type)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
