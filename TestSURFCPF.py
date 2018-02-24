## PLAN:
# FIND AN OBJECT, then do SURF on image, then see how much the points change on the object of interest.... can be any object as long as it's 'large enough'
# find object with contours


import CentralPatternFind as CPF
import cv2
import time
import numpy as np 
from matplotlib import pyplot as plt
import copy


cap = cv2.VideoCapture(0)

while(1):

    _, frame = cap.read()

    ySize = np.shape(frame)[0] # height
    xSize = np.shape(frame)[1] # width
    blackArray = np.zeros((ySize,xSize,3), dtype = np.uint8)

    ########## STEP 1: Contours ...takes larger contours only  
    ########## STEP 2: STABILIZE CONTOURS FOR REPEATABILITY       .... can only move kinda slowly

    for i in range(4):
        _, frame = cap.read()
        imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        ret,thresh = cv2.threshold(imgray,127,255,0)
        image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        bigContours = []
        for c in contours:
            if cv2.contourArea(c) > 500:
                bigContours.append(c)
        if i == 0:
            blackArray0 = cv2.drawContours(copy.copy(blackArray), bigContours, -1, (255,0,0),3)    # blue
        elif i == 1:
            blackArray1 = cv2.drawContours(copy.copy(blackArray), bigContours, -1, (0,0,255),3)    # red 
        elif i == 2:
            blackArray2 = cv2.drawContours(copy.copy(blackArray), bigContours, -1, (0,255,255),3)  # yellow
        elif i == 3:
            blackArray3 = cv2.drawContours(copy.copy(blackArray), bigContours, -1, (0,255,0),3)    # green

    addedImg = cv2.addWeighted(blackArray0,0.5,blackArray1,0.5,0)     # purple is good ... (127,0,127)
    addedImg2 = cv2.addWeighted(blackArray2,0.5,blackArray3,0.5,0)    # lime is good   ... (0,255,127)
    finalImg = cv2.addWeighted(addedImg,0.5,addedImg2,0.5,0)          # gold is good     ... (64,127,127)
    var = 60
    lower_range, upper_range = (64-var,127-var,127-var),(64+var,127+var,127+var)              # this is the range
    mask = cv2.inRange(finalImg,lower_range, upper_range)             # masks it
    output = cv2.bitwise_and(finalImg,finalImg, mask = mask)


    ####  STEP 3: then check color uniformity as in Notes

    img2gray = cv2.cvtColor(output,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of contour in frame
    img1_bg = cv2.bitwise_and(frame,frame,mask = mask_inv)
    # Take only region of contour from contour image.
    img2_fg = cv2.bitwise_and(output,output,mask = mask)
    frameOutput =  cv2.add(img1_bg,img2_fg)

    cv2.imshow('res',dst)
    cv2.imshow('img1_bg',img1_bg)    
    cv2.imshow('contours',frame)
    cv2.imshow('output',output)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        #plt.imshow(fgmask),plt.show()
        break

cap.release()
cv2.destroyAllWindows()