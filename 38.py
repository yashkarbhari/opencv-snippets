# with createBackgroundSubtractorMOG()
import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
# cv2.bgsegm.createBackgroundSubtractorMOG()
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if frame is None:
        break
    fgmask = fgbg.apply(frame)
        
    cv2.imshow('Frame', frame)
    cv2.imshow('FG MASK Frame', fgmask)
    
    keyboard = cv2.waitKey(20)
    if keyboard == 'q' or keyboard == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
-------------------------------------------------------
# with BackgroundSubtractorKNN()

