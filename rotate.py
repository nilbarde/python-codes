import cv2
import numpy as np
import os

read_name = '1.png'
angle = 10 #counter clockwise positive
write_name = '2.png

img = cv2.imread(read_name)
rows , cols , _ = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
img = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite(write_name,img)



