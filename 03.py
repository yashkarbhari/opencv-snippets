import cv2

cap = cv2.VideoCapture(0);

while(True):
    # 'ret' is used to check true or false and frame is used to read the frame
    ret, frame = cap.read()
    
    
    # this converts the videocapture into a gray scale video
    # cv2.cvtColor(source of the image, the converison we want to do)
    # the default color image is BGR and we want to convert it to gray.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    
    # The ''& 0xFF' is a coce in 64 bit computers for the ord() to be used
    # and when we press the 'q' button  it will destroy all the windows 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 


# this releases the capture frames
cap.release()
cv2.destroyAllWindows()
