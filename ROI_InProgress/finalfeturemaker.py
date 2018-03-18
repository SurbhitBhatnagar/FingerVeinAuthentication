import cv2
from array import array
import numpy as np
from os import listdir
from os.path import isfile, join
from collections import Counter
import h5py
#from tempfile import TemporaryFile

mypath=r"/home/chotadon_varun/Desktop/final_phase/allimp_codes/hola"
cropped_images="/home/chotadon_varun/Desktop/final_phase/allimp_codes/cms"
	
#//*---------------------------------------------------------------------------------------------*//	
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
onlyfiles.sort(key=lambda f: int(filter(str.isdigit, f)))
images = np.empty(len(onlyfiles), dtype=object)
county=1
x = np.arange(257)
t = 0

for n in xrange(len(onlyfiles)):#len(onlyfiles)
	
	images[n] = cv2.imread( join(mypath,onlyfiles[n]),0)#put 0 after comma
	print onlyfiles[n]
	img = images[n]
	img = img[38:230,:]
	img2 = cv2.GaussianBlur(img, (5, 5), 0)
	img3 = cv2.medianBlur(img2,5)
	edges = cv2.Canny(img3,55,90)	
	county=county+1
	
	# Detect contours using both methods on the same image
	contourimage,contours,hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
	contours2,contoursagain , hierarchyagain= cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	# Copy over the original image to separate variables
	image1 = img.copy()
	
	# Draw both contours onto the separate images
	cv2.drawContours(image1,contours, -1, (255,255,255), 1)
	totalcontours = len(contours)-1
	
	a = array("i") #Thisis array to store contour length 
	b = array("i") #This is array to store final biggest contours we obtained
	
	for r in range (0,totalcontours):
		contlen =len(contours[r])
		a.append(contlen)
		
	c = sorted(a,reverse=True) #This will print a in decending order to get the greatest two contours 
	
	
	for r in range (0,totalcontours):
		if len(contours[r]) == c[0]:
		#print (r,"this is the greatest contour")
			b.append(r)

		elif len(contours[r])== c[1]:
		#print (r,"this is the second greatest contour")
			b.append(r)

	
	bigcont = contours[b[0]]
	smallcont = contours[b[1]]
	
	reqdim = np.shape(smallcont)
	
	
	resized_bigcont = np.resize(bigcont,reqdim)	
	subtraction = abs(resized_bigcont-smallcont)	
	vertical_distance = array("i") #Only to get a Min vertical Distance
	bigcont_vertdist = array("i")
	
	for x in range (0,len(subtraction)):
		vertical_distance.append(subtraction[x,0][1]) #This will print all the column diff values
		
	
	finalrow = array("i") #FINAL ROW HERE
	
	shortestdist = min(vertical_distance)
	
	final_col_array = array("i")
	
	for q in range(0,len(vertical_distance)):
		if subtraction[q,0][1] == shortestdist:
			final_col_array.append((resized_bigcont[q,0][1]))		#This will give you the col value you need to crop the image
			#coz row values will be from 0 to :
	
	
	final_col_point_needed = final_col_array[0]


	cropped = img[final_col_point_needed - shortestdist :final_col_point_needed,60:160] #Assuming the finger width 
	#cv2.imwrite(join(cropped_images,onlyfiles[r]),cropped)			
	img=cropped
	#img= im[60:80,200:220]		#last 20 columns not being read
	iar=np.array(img)

	row,col=img.shape #r=rows, c=columns
	#d=im.ndim

	#possible error will be in r and c values , when actual implementation (or) when r,c are not multiples of 5


	#print (r,c)
	y=np.zeros((5,5))
	z=np.zeros((3,3))
	u=np.zeros((3,3))
	v=np.zeros((3,3))
	fvpos=array('f')
	fvneg=array('f')


	def algo(immat,cent,z):
		##########################Matrices Declaration#######################################
		
		#wm=np.zeros((3,3))

		#print "y is :\n",y

		

		############################Binary Pattern###########################################
		y[0,0] = immat[0,0]-immat[1,1]
		y[0,2] = immat[0,2]-immat[1,2]
		y[0,4] = immat[0,4]-immat[1,3]
		y[2,0] = immat[2,0]-immat[2,1]
		y[2,4] = immat[2,4]-immat[2,3]
		y[4,0] = immat[4,0]-immat[3,1]
		y[4,2] = immat[4,2]-immat[3,2]
		y[4,4] = immat[4,4]-immat[3,3]

		y[1,1] =immat[1,1]-cent
		y[1,2] =immat[1,2]-cent
		y[1,3] =immat[1,3]-cent
		y[2,1] =immat[2,1]-cent
		y[2,3] =immat[2,3]-cent
		y[3,1] =immat[3,1]-cent
		y[3,2] =immat[3,2]-cent
		y[3,3] =immat[3,3]-cent

		#print y

		for r in range (0,5):
			for c in range(0,5):
					if y[r,c]>0:
						y[r,c]=1
					else :
						y[r,c]=2
		
		#print "Binary Pattern\n",y


		###################################Ternary Pattern###########################################
		if y[0,0]==y[1,1] :
			z[0,0]=y[0,0]
		else :
			z[0,0]=0

		if y[0,2]==y[1,2]:
			z[0,1]=y[0,2]
		else:
			z[0,1]=0

		if y[0,4]==y[1,3]:
			z[0,2]=y[0,4]
		else:
			z[0,2]=0

		if y[2,4]==y[2,3]:
			z[1,2]=y[2,4]
		else:
			z[1,2]=0

		if y[4,4]==y[3,3]:
			z[2,2]=y[4,4]
		else:
			z[2,2]=0

		if y[4,2]==y[3,2]:
			z[2,1]=y[4,2]
		else:
			z[2,1]=0

		if y[4,0]==y[3,1]:
			z[2,0]=y[4,0]
		else:
			z[2,0]=0

		if y[2,0]==y[2,1]:
			z[1,0]=y[2,0]
		else:
			z[1,0]=0	

	#	print"Ternary Pattern\n", z

		#####################################+ve Matrix#######################################

		for r in range(0,3):
			for c in range(0,3):
					if z[r,c]==1:
						u[r,c]=1
					else:
						u[r,c]=0

		#print "+ve Matrix \n",u

		###################################-ve Matrix#######################################

		for r in range(0,3):
			for c in range(0,3):
					if z[r,c]==2:
						v[r,c]=1
					else:
						v[r,c]=0

		#print"-ve Matrix\n", v


		###################################Weighted Matrix#######################################
		wm=[[0 for j in range(3)] for j in range(3)]
		'''
		wm[0][0]=8
		wm[0][1]=4
		wm[0][2]=2
		wm[1][0]=16
		wm[1][2]=1
		wm[2][0]=32
		wm[2][1]=64
		wm[2][2]=128
		'''
		wm[0][0]=8
		wm[0][1]=4
		wm[0][2]=2
		wm[1][0]=16
		wm[1][2]=1
		wm[2][0]=32
		wm[2][1]=64
		wm[2][2]=128

		#print "Weight\n", wm

		################################## LTCoP-1################################################
		'''
		for r in range(0,3):
			for c in range(0,3):
					while(u[r,c]!=0):
						pr=u[r,c]*wm[r,c]
					sum=sum+pr

		print sum
		'''

		r1 =wm[0] * u[0]
		s1=wm[1]  * u[1]
		t1=wm[2]  * u[2]
		ltcop1=np.sum(r1)+np.sum(s1)+np.sum(t1)

		#print "LTCoP 1 is :", ltcop1

		################################### LTCoP-2################################################

		r2 =wm[0] * v[0]
		s2=wm[1]  * v[1]
		t2=wm[2]  * v[2]
		ltcop2=np.sum(r2)+np.sum(s2)+np.sum(t2)

		#print"LtCoP 2 is :", ltcop2
		fvpos.append(ltcop1)
		fvneg.append(ltcop2)
		#time.sleep(0.02)

	count=0
	for m in range (0,row-4):
		for n in range (0,col-4):
			immat=iar[m:m+5,n:n+5]	
			#print immat
			#print count		
			cent=immat.item(12)
			algo(immat,cent,z)		
			count=count+1
	#print fvpos
	#print fvneg
	a=len(fvpos)
	b=len(fvneg)
	#print iar
	#print img
	#print (row,col)
	#print a
	#print b		

	###############################################################################################################################################
	#cv2.imshow('matimg',img)
	###############################################################################################################################################
	'''
	def histogram(fvpos):
		d={}
		for k in fvpos:
			if k in d:
				d[k] += 1
			else:
				d[k] = 1
		return d
	print d
	'''
	cnt1 = Counter(fvpos)
	#print"feature 1 is :\n",cnt1
	hs1 ,x=np.histogram(fvpos,bins=range(257))
	#print (type(hs1),"hs1")
	#print hs1
	#print (type(x),"x")
	#print x
	
	#print "Final FV Histogram for LTcop +ve: ",hs1

	cnt2 = Counter(fvneg)
	#print"feature 2 is :\n",cnt2
	hs2,y=np.histogram(fvneg,bins=range(257))
	#print "Final FV Histogram for LTcop -ve: ",hs2
	#print len(cnt1)
	#print len(cnt2)
	#print ("no of images :",county)#county,
	fvec=np.concatenate((hs1,hs2),axis=0)
	print str(t)
	with h5py.File('histo.h5', 'a') as hf: 	
		hf.create_dataset(str(t),data=(fvec))
		#hf.create_dataset('hs2',data=hs2)
		hf.close()
	t += 1
