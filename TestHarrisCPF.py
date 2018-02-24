import CentralPatternFind as CPF
import cv2
import time
import numpy as np 
from matplotlib import pyplot as plt
import copy


cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    #print (np.shape(frame)[0])
    ySize = np.shape(frame)[0] # height
    xSize = np.shape(frame)[1] # width
    blackArray = np.zeros((ySize,xSize,3), dtype = np.uint8)
    whiteArray = np.ones((ySize,xSize,3), dtype = np.uint8)

    # find and draw the keypoints
    harrisImg = copy.copy(frame)

    grayHarrisImg = np.float32(cv2.cvtColor(harrisImg,cv2.COLOR_BGR2GRAY))
    dst = cv2.cornerHarris(grayHarrisImg,2,3,0.04)
    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    frame[dst>0.01*dst.max()]=[0,0,255]
    ### Which is basically the same as :
    ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
    cv2.imshow('harry',frame)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        #plt.imshow(fgmask),plt.show()
        break

cap.release()
cv2.destroyAllWindows()