import string
from turtle import color, width
import cv2 as cv
from fer import FER
cam=cv.VideoCapture(0)
img=cam.read()
emotion_detector=FER(mtcnn=True)
analysis=emotion_detector.detect_emotions(img[1])
print(analysis)
cv.putText(img[1],str(analysis[0]['emotions']),(40,20),cv.FONT_HERSHEY_COMPLEX_SMALL,0.45,(0,0,0),1,cv.LINE_AA)
cv.imshow("EMOTION",img[1])
cv.waitKey(0)