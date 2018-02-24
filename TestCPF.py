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

    # Initiate FAST object with default values                                 #### basically can use FAST or Harris for edge detection 
    fast = cv2.FastFeatureDetector_create(threshold=25)
    # find and draw the keypoints
    kp2 = fast.detect(frame,None)
    cornerImg = copy.copy(frame)
    cornerImg = cv2.drawKeypoints(cornerImg, kp2, None,color=(255,250,20))
    testImgInput1 = cv2.drawKeypoints(whiteArray, kp2, None,color=(255,250,20))
    greyImgInput1 = cv2.cvtColor(testImgInput1,cv2.COLOR_BGR2GRAY)

    cv2.imshow('corners', cornerImg)
    cv2.imshow('testImgInput1',greyImgInput1)    # GREeeeeat for first input of central shape finder 
    

    #objectCPF = CPF.CPF(greyImgInput1,(ySize,xSize), kp2)
    objectCPF = CPF.CPF()
    #centralWindow = objectCPF.getCentralWindow(greyImgInput1)
    centralPoint = objectCPF.findCentralPixel(greyImgInput1)
    #centralWindowCentralPoint = objectCPF.findCentralPixel(centralWindow)

    #print (centralPoint)
    localizeImg = cv2.circle(frame, centralPoint, 3, (255,0,0), -1)          ### circle is off rn sad boys 
    #localizeImg2 = cv2.circle(centralWindow, centralWindowCentralPoint, 3, (255,255,0), -1)  
    cv2.imshow('testpoint',localizeImg)
    #cv2.imshow('small',localizeImg2)
    """kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(greyImgInput1,kernel,iterations = 1)
    erosion = cv2.erode(dilation,kernel,iterations = 2)
    cv2.imshow('dilate',erosion)"""

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        #plt.imshow(fgmask),plt.show()
        break

cap.release()
cv2.destroyAllWindows()