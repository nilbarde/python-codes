import cv2
import numpy as np
from os import walk,path

fold = path.dirname(path.realpath(__file__))
fold = fold +'/'
print (fold)

image_names = []
for (dirpath,dirnames,filenames) in walk(fold):
	for name in filenames:
		if(name.endswith('.png')):
			image_names.append(name)
	break

for name in image_names:
	img = cv2.imread(fold+name)
	cv2.imshow('img',img)
	colors = np.arange(16*16*16).reshape(16,16,16)
	for i in range (200):
		for j in range (200):
			x=img[i][j]
			colors[x[0]/16][x[1]/16][x[2]/16]+=1

	colors[0][0][0]=0
	
	colors[1][0][0]=0
	colors[0][1][0]=0
	colors[0][0][1]=0
	
	colors[1][1][0]=0
	colors[0][1][1]=0
	colors[1][0][1]=0

	colors[1][1][1]=0

	colors[15][15][15]=0
	
	colors[14][15][15]=0
	colors[15][14][15]=0
	colors[15][15][14]=0
	
	colors[14][14][15]=0
	colors[15][14][14]=0
	colors[14][15][14]=0

	colors[14][14][14]=0

	max_area=0
	for i in range (16):
		for j in range (16):
			for k in range (16):
				if(colors[i][j][k]>0):
					blue_val = i*16
					green_val = j*16
					red_val = k*16

					lower = np.array([(blue_val-25),(green_val-25),(red_val-25)])
					upper = np.array([(blue_val+25),(green_val+25),(red_val+25)])
	
					mask = cv2.inRange(img,lower,upper)
					_,contours,_ = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
					for con in contours:
						area = cv2.contourArea(con)
						if (area>max_area):
							large = con
							max_area = area

	cv2.drawContours(img,large,-1,(0,255,0),2)

	cv2.imshow('con',img)
	me = 0
	while (me!=113):
		me = cv2.waitKey(20)

