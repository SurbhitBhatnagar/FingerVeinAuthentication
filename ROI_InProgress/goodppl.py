#################################################CLASSIFICATION USING KNN CLASSIFIER###########################################################

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
from sklearn.neighbors import KNeighborsClassifier

hf = h5py.File('histo.h5', 'r')	


p=np.arange(5)	#=no_classes
A=np.repeat(p,4)	#=no of trainers
a=len(hf)
print"\ntotal length :", a
P=0
b=0
q=0

darray=np.array([])
karray=np.array([])
O=np.array([])
q=iter(xrange(a))
#test_arr=np.array([])


q=iter(range(a))
for t in q:
	for P in range(0,5):			#params (0, no. of classes)
		if t==(3+(6*P)):
			q.next()
			q.next()
	P+=1	
	d=hf.get(str(t))
	k=np.array(d)
	O=np.append(O,[k])

k=np.mat(O)
k.shape=(20,512)		#.shape(no.of train images, 512)
print "\nlength of training data :",len(k)

neigh = KNeighborsClassifier(n_neighbors=3,weights='distance', p=1)		#p=1 for euclidean; p=2 for manhattan
#neigh=KNeighborsClassifier(n_neighbors=5, weights='distance', algorithm='ball_tree', leaf_size=20, p=1, metric='minkowski', metric_params=None, n_jobs=1)
neigh.fit(k, A) 



t=0	
g=0
while(t<=25):			#t<= last image no - 4
	try:
		t+=4
		print t
		d1=hf.get(str(t))
		k1=np.array(d1)
		print k1
		t+=1
		d2=hf.get(str(t))
		k2=np.array(d2)
		print t
		print k2
		with h5py.File('testhisto_for goodppl.h5', 'a') as hf2: 	
			hf2.create_dataset(str(g),data=k1)
			g+=1
			hf2.create_dataset(str(g),data=k2)
			print "DONE"
			hf2.close()	
		g+=1
		t+=1
	except:
		print("baaps")
		
#print "length of test data :",len(karray),"\n",karray
#hf2.close()
fd=0
z=0


hf3 = h5py.File('testhisto_for goodppl.h5', 'r')	
u=len(hf3)
r=0

Larray=array("i")
g=iter(range(u))
for f in g:
	d4=hf3.get(str(f))
	k4=np.array(d4)							
	L=neigh.predict(k4)   					      
	print 'class of image {} is {}'.format(f,L)		 	
	Larray.append(L)					
	op=np.asarray(Larray)
	v=len(op)
	
	 
#print L
#print s

print"\n Final Classification Result:",op
'''
s=0
for r in range (0, 269, 2):     #range(start_point, end_point, step size)
	if op[r]!=op[r+1]:
		s=s+1
		
print"\n no of imposters :", s
print "\nlen is :",v
'''
