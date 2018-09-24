import numpy as np
import random
import cv2
from tqdm import tqdm

def fill_me(image,x_co,y_co,color=[0,0,0],size=1):
	global height
	global width
	w_fill = int(x_co*(height/10) + width/2)-1
	h_fill = int(y_co*(height/10)*(-1)+height)-1
	#print(h_fill,w_fill)
	image[h_fill,w_fill,:]=color
	return image

def give_me_next_point(x,y,n):
	if(n==1):
		x_new = 0
		y_new = 0.16*y
	elif(n==2):
		x_new = 0.85*x + 0.04*y
		y_new = (-1)*0.04*x + 0.85*y + 1.6
	elif(n==3):
		x_new = 0.2*x + (-1)*0.26*y
		y_new = 0.23*x + 0.22*y + 1.6
	else:
		x_new = (-1)*0.15*x + 0.28*y
		y_new = 0.26*x + 0.24*y + 0.44

	return x_new,y_new

prob_array=[]
for i in range(1):
	prob_array.append(1)
for i in range(85):
	prob_array.append(2)
for i in range(7):
	prob_array.append(3)
for i in range(7):
	prob_array.append(4)
#225
x,y = 0,0
global height
global width
height = 700
width = 700
base_image = np.zeros((height,width,3),dtype='uint8')
iterations = 1000000

for i in tqdm(range(iterations/10)):#889093500 15khe5
	base_image = fill_me(base_image,x,y,[0,255,0])
	n = random.choice(prob_array)
	x,y = give_me_next_point(x,y,n)
	if((i+1)%5==0):
		cv2.imshow('barnsley fern',base_image)
		cv2.waitKey(1)
	if((i+1)%100000==0):
		cv2.imwrite('leaf'+str(i+1)+'.png',base_image)

for i in tqdm(range(iterations/10,iterations)):#889093500 15khe5
	base_image = fill_me(base_image,x,y,[0,255,0])
	n = random.choice(prob_array)
	x,y = give_me_next_point(x,y,n)
	if((i+1)%100==0):
		cv2.imshow('barnsley fern',base_image)
		cv2.waitKey(1)
	if((i+1)%100000==0):
		cv2.imwrite('leaf'+str(i+1)+'.png',base_image)

cv2.imwrite('leaf.png',base_image)
cv2.waitKey(0)

'''
1
0.85 85
0.2 7
-0.15 7
'''

