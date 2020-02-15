# -*- coding: utf-8 -*-
import cv2
img = cv2.imread('a.jpg')
from matplotlib import pyplot as plt
plt.imshow(img) 
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB )
plt.imshow(img1) 

learner = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
face = learner.detectMultiScale(img1, 1.3, 5)
print(face)

for(a,b,c,d) in face:
    cv2.rectangle(img1,(a,b),(a+c,b+d),(255,255,0),3)

plt.imshow(img1)

cv2.waitKey(0)