import string
from turtle import color, width
import cv2 as cv
from fer import FER
img=cv.imread("C:\\Users\\paars\\Downloads\\fear.jpg")
def PreProcessing(frame,scale=2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    frame=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
    frame=cv.GaussianBlur(frame,(3,3),cv.BORDER_DEFAULT)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_LINEAR)
img_processed=PreProcessing(img)
emotion_detector=FER(mtcnn=True)
analysis=emotion_detector.detect_emotions(img_processed)
print(analysis)
cv.putText(img_processed,str(analysis[0]['emotions']),(40,20),cv.FONT_HERSHEY_COMPLEX_SMALL,0.75,(0,0,0),1,cv.LINE_AA)
cv.imshow("EMOTION",img_processed)
cv.waitKey(0)