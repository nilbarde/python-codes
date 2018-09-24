import cv2
import random
import numpy as np

def fill_me(image,x_co,y_co,color=[0,0,0],size=3):
	image[x_co-(size/2):x_co+(size/2),y_co-(size/2):y_co+(size/2),:]=color
	return image

base_image = np.zeros((600,900,3),dtype='uint8')
base_image.fill(255)
base_image[:1,:].fill(0)
base_image[598:,:].fill(0)
base_image[:,0:1].fill(0)
base_image[:,898:].fill(0)

number_of_points = 0
#print('input number of points')
number_of_points = 3
x_co = []
y_co = []
'''
for i in range(number_of_points):
	#print('please input co-ordinates of point ' + str(i+1))
	#x = int(raw_input())
	#y = int(raw_input())
	x_co.append(x)
	y_co.append(y)
	base_image = fill_me(base_image,x,y,[255,0,0],7)

print('please input co-ordinates of pointer')

x_pointer = int(raw_input())
y_pointer = int(raw_input())
'''
x_co = [100,500,500]
y_co = [450,100,800]
for i in range(number_of_points):
	x=x_co[i]
	y=y_co[i]
	base_image = fill_me(base_image,x,y,[255,0,0],7)
x_pointer = 300
y_pointer = 450
base_image = fill_me(base_image,x_pointer,y_pointer,[0,0,0],5)

approach_frac = 0.5

approach_point = 100
iterations = 15000

print(x_co,y_co)
print('input point to approach')
aproach_point = int(raw_input())
while(aproach_point!=-1):
	print('approaching point ' + str(aproach_point),x_co,y_co)
	aproach_point-=1
	print(x_pointer,y_pointer)
	x_pointer = int(x_co[aproach_point]*(approach_frac) + x_pointer*(1 - approach_frac))
	y_pointer = int(y_co[aproach_point]*(approach_frac) + y_pointer*(1 - approach_frac))
	base_image = fill_me(base_image,x_pointer,y_pointer,[0,0,0])
	print(x_co[aproach_point],y_co[aproach_point])
	print(x_pointer,y_pointer)
	cv2.imshow('fractals',base_image)
	cv2.waitKey(0)
	print('input point to approach')
	aproach_point = int(raw_input())
print('out of first while loop')	

for i in range(iterations):
	aproach_point=random.randint(0,number_of_points-1)
	print(str(i) + ' -: approaching point ' + str(aproach_point+1))	
	x_pointer = int(x_co[aproach_point]*(approach_frac) + x_pointer*(1 - approach_frac))
	y_pointer = int(y_co[aproach_point]*(approach_frac) + y_pointer*(1 - approach_frac))
	base_image = fill_me(base_image,x_pointer,y_pointer,[0,0,0])
	cv2.imshow('fractals',base_image)
	cv2.waitKey(1)
print('out of for loop')

cv2.imshow('sierpinski triangle',base_image)
cv2.waitKey(0)


