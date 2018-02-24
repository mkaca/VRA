#TRY TO USE SOMETHING OTHER THAN FAST


## input : pixels of desire (from fast)                                DONE
           #image size                                                 DONE
""" output: largest shape in the middle (cluster of points)
            and size of middle shape in pixels (height and width)
  magic: a. focus on central part of window ( see book)                 DONE
         b. exclude outlier clusters and choose cluster with:

                find closest point to the center                       DONE
                choose X amoutn of points closest to it
                If abs((median of distaneces) - (mean of distances)) > thresholdY, then discard furthest point to make amoutn of points (X-1) and try again... keep doing until thresholdY is met. 
                       If cluster size gets below N due to the reduction algo, then try using a different point in one of the 'corners' of the central part of window, and repeat algo

                optional params: X, ThresholdY, N, 

        c. Once cluster is chosen, identify its size and do some mods to it like erosion and dilution to get general cluster shape (# of sides and corners) ...which will be used for future frames --> for identifying distance change!!   

        PROBLEMS:    the shape has to be consistent in between frames..there are slight variations from interest points from frame to frame (can get median of frames or seomething like that)
"""
import cv2 
import numpy as np 
from math import sqrt

class CPF(object):
	# inputImg type : points of interest on white background, size: (y,x,3)
	# size type:  ySize (height), xSize (width)
	def __init__(self):
		#init params
		#self.inputImg = inputImg
		#if (int(np.shape(inputImg)[0]) != int(size[0]) or int(np.shape(inputImg)[1]) != size[1]):
			#raise ValueError('size does not match image...imageSize: %i,%i and sizeInputted: %i,%i'%(np.shape(inputImg)[0],np.shape(inputImg)[1],size[0],size[1]))
		pass

	def getCentralWindow(self, inputImg, proportionFactorEdgeTrim = 4):  # for example, the PFET = 4 trims 1/4 of the window size from all directions, PFET = 6 trims 1/6 of window size from all directions
		ySize = np.shape(inputImg)[0]
		xSize = np.shape(inputImg)[1]
		yFrag = int(ySize / proportionFactorEdgeTrim)
		xFrag = int(xSize / proportionFactorEdgeTrim)
		croppedImg = inputImg[yFrag:ySize-yFrag,xFrag:xSize-xFrag]
		return croppedImg
		#cv2.waitKey(0)


	def findCentralPixel(self, img):    # used to find central pixel of the kp array 
		#get middle point
		yMid = int(np.shape(img)[0] / 2)    # y
		xMid = int(np.shape(img)[1] / 2)    # x

		#get kp Array
		newKp = self.convertKPImagetoArray(img)
		olderDistance = 10000
		centralPoint = (None, None)
		for x,y in newKp:
			distance = sqrt((x-xMid)**2 + (y-yMid)**2)
			if distance < olderDistance:
				olderDistance = distance
				centralPoint = (x,y)
		print (centralPoint)
		return centralPoint


	def convertKPImagetoArray(self,img):     ### input must be greyscale image of kp pixels on black background
		newKp = []
		for row in range(len(img)):
			for y in img[row]:
				if y != 1:
				   newKp.append((row,y))  # sorted by lowest x to highest x, so goes from left to right on an image
		return newKp






