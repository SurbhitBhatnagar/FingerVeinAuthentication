import cv2
from array import array
import numpy as np

img = cv2.imread('test2.bmp')
retval , threshold = cv2.threshold(img, 70,255,cv2.THRESH_BINARY) #Anything above 100 will be white

#img2 = cv2.imread('test2.bmp')
#retval2 , threshold2 = cv2.threshold(img2, 70,255,cv2.THRESH_BINARY) #Anything above 100 will be white

#print img.shape
#print img2.shape

#rows,cols,channels = threshold.shape
a = array("i")
b = array("i")
for x in range (0,240):
		sum = np.sum(threshold[x,:])
		if (sum == 244800):
			a.append(x)
			b.append(sum)
			

			
print(a)
print(b)
firstwhite = a[0]
lastwhite = a[-1]

print(firstwhite)
print(lastwhite)

cropped = img[firstwhite:lastwhite , :]		
#cv2.imshow('threshold',threshold)
cv2.imshow('img1',img)
cv2.imshow('cropped',cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

		
		



































