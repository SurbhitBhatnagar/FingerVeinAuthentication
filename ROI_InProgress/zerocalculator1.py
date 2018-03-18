import cv2
from array import array
import numpy as np
from os import listdir
from os.path import isfile, join
from collections import Counter
import h5py
from sklearn import svm
import itertools
import time
a=0
t=0
P=0
d=0
k=0
i=0
hf = h5py.File('allhisto.h5', 'r')	
a=len(hf)
for P in range(0,810):			#param (0, total no. images)
	d=hf.get(str(P))
	k=np.array(d)
	if(sum(k)<50):
		i+=1
		print k		
	#P+=1	
	
print ":",i	
