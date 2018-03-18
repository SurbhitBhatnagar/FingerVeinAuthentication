##############################################CLASSIFICATION USING KNN CLASSIFIER WITH IMPOSTER CALCULATION CODE#####################################
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


p=np.arange(135)	#=no_classes
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
	for P in range(0,135):
		if t==(3+(6*P)):
			q.next()
			q.next()
	P+=1	
	d=hf.get(str(t))
	k=np.array(d)
	O=np.append(O,[k])

k=np.mat(O)
k.shape=(40,512)	#.shape(no.of train images, 512)
print "\nlength of training data :",len(k)

neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(k, A) 



t=0	
g=0
while(t<=55):
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
		with h5py.File('testhisto.h5', 'a') as hf2: 	
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


hf3 = h5py.File('testhisto.h5', 'r')	
u=len(hf3)
r=0

Larray=array("i")
g=iter(range(u))
for f in g:
	d4=hf3.get(str(f))
	k4=np.array(d4)
	L=neigh.predict(k4)   # CHECK IF L CAN BE WRITTEN IN THE FORM OF L(f)
	print 'class of image {} is {}'.format(f,L)
	Larray.append(L)
	op=np.asarray(Larray)
	v=len(op)
	print "\nlen is :",v
	 
#print L
#print s

print"\n it is:",op
s=0
for r in range (0, 19, 2):     #range(start_point, end_point, step size)
	if op[r]!=op[r+1]:
		s=s+1
		
print"\n no of imposters :", s


'''
g=iter(range(u))
for f in g:
	d4=hf3.get(str(f))
	k4=np.array(d4)
	L=neigh.predict(k4)
	print L

s=0
g=iter(range(u))
for f in g:
#d4=hf3.get(str(f))
#k4=np.array(d4)
#L(f)=neigh.predict(k4)   # CHECK IF L CAN BE WRITTEN IN THE FORM OF L(f)
	L(f)=neigh.predict(np.array(hf3.get(str(f))))
	print 'class of image {} is {}'.format(f,L)
	for f in range (0,u-2):     # f has to increment by 1 to count the last element so instead of range(0,u-1)...(0,u-2)
		if L(f)!=L(f+1):
			print 'class{} do not match {}'.format(L(f),L(f+1))
			s=s+1   
	print L,f

for z in range (20):
	fd=karray[z]
	#print fd.shape
	d=hf.get(str(fd))
	darray=np.array(d)[np.newaxis]
	darray.T
	L=lin_clf.predict(darray)
	#time.sleep(0.7)
	print fd 
	#print d
	print 'class of image{} is {}'.format(f,L)

z=karray(0)
d=hf.get(str(z))
darray=np.array(d)
L=lin_clf.predict(darray)
print 'class of image{} is {}'.format(f,L)
'''




