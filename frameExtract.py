import cv2
import os

cap1 = cv2.VideoCapture(0);
i=1
while True:
    ret, frames1 = cap1.read()
    cv2.imshow("Frames",frames1);
    cv2.imwrite(os.path.join("static/images/",str(i)+".jpg"),frames1)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break;
    i=i+1
cap1.release();
cv2.destroyAllWindows();
