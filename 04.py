import cv2

cap = cv2.VideoCapture(0);
# fourcc is a 4 bit code which is used to specify the video codec. 
# Use the *XVID as a default fourcc code 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# VideoWriter() is used for saving the file, 1st argument is the output file
# name, the second argument is the fourcc code, the 3rd argument is the 
# no. of frames per sec, and the fourth argument is size of the frame.
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# is.Opened() is used to check if the file is opened or not
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
