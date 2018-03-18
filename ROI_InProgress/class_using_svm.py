##############################################PROGRAM FOR CLASSIFICATION USING SVM CLASSIFIER######################################################
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


hf = h5py.File('allhisto.h5', 'r')	


p=np.arange(135)	#=no_classes
A=np.repeat(p,4)	#=no of trainers
a=len(hf)
#print"\ntotal length :", a, "\n target is :\n",A
P=0
b=0
q=0

darray=np.array([])
karray=np.array([])
O=np.array([])

q=iter(xrange(a))
for t in q:
	for P in range(0,135):			#params (0, no. of classes)
		if t==(3+(6*P)):
			q.next()
			q.next()
	P+=1	
	d=hf.get(str(t))
	k=np.array(d)
	O=np.append(O,[k])

k=np.mat(O)
k.shape=(540,512)			#params(no of trainers, 512)
#print "\nlength of training data :",len(k)

lin_clf1=svm.LinearSVC()
lin_clf1.fit(k,A)



t=0	
g=0

while(t<=804):
	try:
		t+=4
		print t
		d1=hf.get(str(t))
		k1=np.array(d1)
		#print k1
		t+=1
		d2=hf.get(str(t))
		k2=np.array(d2)
		print t
		#print k2
		with h5py.File('alltesthisto.h5', 'a') as hf2: 	
			hf2.create_dataset(str(g),data=k1)
			g+=1
			hf2.create_dataset(str(g),data=k2)
			print "DONE"
			hf2.close()	
		g+=1
		t+=1
	except:
		print("Executed")
	



hf3 = h5py.File('alltesthisto.h5', 'r')	
u=len(hf3)
#print "\n length of test data is :",u
m=iter(range(u))
for f in m:
	d4=hf3.get(str(f))
	k4=np.array(d4)
	#time.sleep(0.5)
	L=lin_clf1.predict(k4)
	print L
	
	

