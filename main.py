import cv2
cap=cv2.VideoCapture(0)
while True:
    frame,ret=cap.read()
    ret=cv2.flip(ret,1)
    cv2.imshow("Frame",ret)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()