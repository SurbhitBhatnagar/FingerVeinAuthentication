import cv2
from array import array
import numpy as np
import os,sys
from multiprocessing import Pool

#Open A file 

#incomming_images = "/home/kbslalith/Desktop/Final Year Project/FVD-Project-/ROI_InProgress/veinimages"  #Change this according to where you are coding
#cropped_images= "/home/kbslalith/Desktop/Final Year Project/FVD-Project-/ROI_InProgress/croppedimages"

#dirs = os.listdir( incomming_images )

#for file in dirs:
 #  print file #To Print all the file names 

#print len(dirs) #Prints the lenggth of the Directory   







img = cv2.imread('1001.bmp')
retval , threshold = cv2.threshold(img, 70,255,cv2.THRESH_BINARY) #Anything above 70 will be white

#img2 = cv2.imread('test2.bmp')
#retval2 , threshold2 = cv2.threshold(img2, 70,255,cv2.THRESH_BINARY) #Anything above 70 will be white

#print img.shape #To Find the number of rows and columns i.e Pixels  ----- We got [240*320].Same For All.
#print img2.shape

#rows,cols,channels = threshold.shape / Not needed just for reference . 

a = array("i") #To create an empty array ready to take integer values . 
b = array("i")
for x in range (0,240): #This is how you do For Loop In Python
		sum = np.sum(threshold[x,:]) # This will give us the sum of all pixel values row after row
		if (sum == 244800): # This is the best part . 255*3 For Pixel and 255*3*320 coz 320 columns are there
			a.append(x)     #Take Care of the Tabs , they will make a lot of difference to the output . This is Python
		#b.append(sum)  #Just for verifying , not needed in the actual code.
			

			
#print(a)
#print(b)
firstwhite = a[0] #This is how you get the first element of the array 
lastwhite = a[-1] #This is for getting the last element of the array 

print(firstwhite) #Just to verify
print(lastwhite)  #Same Obviously . 

cropped = img[firstwhite:lastwhite , :]		#Using the above values we crop the actual image . 
cv2.imshow('threshold',threshold)
cv2.imshow('img1',img) #This is the actual Image , Not needed to show in the actual Code
cv2.imshow('cropped',cropped) #This is the cropped Image . 

cv2.waitKey(0) #This will wait for any key to be pressed
cv2.destroyAllWindows() #If pressed it will close all windows which are open 

		
		



































