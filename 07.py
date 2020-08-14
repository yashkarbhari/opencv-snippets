import cv2

cap = cv2.VideoCapture(0)
# it gives us the width of the frame
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# it gives  us the height of the frame
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# we can set the width and height for the frame using the following function
# set(propID, value for the propID)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
