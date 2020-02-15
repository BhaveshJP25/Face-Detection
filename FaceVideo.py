# -*- coding: utf-8 -*-
import cv2

cap = cv2.VideoCapture(0)

learner = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while 1:
    ret,img=cap.read()
    face=learner.detectMultiScale(img,1.3,5)
    for(a,b,c,d) in face:
        cv2.rectangle(img,(a,b),(a+c,b+d),(222,0,0),5)
    cv2.imshow("BhaveshFrame",img)
    key= cv2.waitKey(30) & 0xff
    if key == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()
    
