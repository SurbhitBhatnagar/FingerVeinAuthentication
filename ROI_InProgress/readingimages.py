import os
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#Open A file 

incomming_images = "/home/kbslalith/Desktop/Final Year Project/FVD-Project-/ROI_InProgress/veinimages"  #Change this according to where you are coding
cropped_images= "/home/kbslalith/Desktop/Final Year Project/FVD-Project-/ROI_InProgress/croppedimages"

dirs = os.listdir(incomming_images)
#for file in dirs:
	#print (file)

x =   len(dirs) #Prints the lenggth of the Directory

#for i in range(1,x):

print (dirs[0])
img = cv2.imread(dirs[0])
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWiindows()