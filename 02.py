import cv2

cap = cv2.VideoCapture(0);

while(True):
    # 'ret' is used to check true or false and frame is used to read the frame
    ret, frame = cap.read()
    
    cv2.imshow('frame', frame)
    
    # The ''& 0xFF' is a coce in 64 bit computers for the ord() to be used
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


# this releases the capture frames
cap.release()
cv2.destroyAllWindows()
        
