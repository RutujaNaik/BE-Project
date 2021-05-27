# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 20:58:11 2020

@author: harsh
"""

#EXTRACTING STILLS FROM THE VIDS

import cv2
import math

#this is input path
videoFile = "C:\\Users\\harsh\\Desktop\\vid5.avi"

#this is the output path
imagesFolder = "C:\\Users\harsh\\Documents\\Programming\\PROJECTS\\BEProj_Enhanced_ATM\\codes\\dataset\\real"

#extraction
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5) #frame rate
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    ret, frame = cap.read()
    if (ret != True):
        break
    if (frameId % math.floor(frameRate) == 0):
        filename = imagesFolder + "/image5_" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print("Done!") 