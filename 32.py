import cv2
import numpy as np
import matplotlib.pyplot as plt 


# A function for the region_of_interest mask's the image with the vertices
def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

# this function is used to draw the lines
def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

    for line in lines:
        for  x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (255, 255, 0), thickness=3)
    
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img

# img = cv2.imread('road5.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
def process(img):

    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    # vertices of the masked part of the image
    region_of_interest_vertices = [
        (0, height),
        (width/2,height/2),
        (width, height)
    ]

    # convert to gray-scale image and apply canny edge detection
    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 120)
    cropped_image = region_of_interest(canny_image, 
                    np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image, 
                           rho = 2,
                           theta = np.pi/60,
                           threshold = 50,
                           lines=np.array([]), 
                           minLineLength = 40, 
                           maxLineGap = 100)

    image_with_lines = draw_the_lines(img, lines)
    return image_with_lines

cap = cv2.VideoCapture('test2.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
cv2.destroyAllWindows()
