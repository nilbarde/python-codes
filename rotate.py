import cv2
import numpy as np
import os

name = '1.png'

img = cv2.imread(name)
rows , cols , _ = img.shape

angle = 10 #counter clockwise positive

M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
img = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite(name,img)



