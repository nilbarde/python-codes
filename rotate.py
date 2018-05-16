import cv2
import numpy as np
import os

img = cv2.imread('1.png')
rows , cols , _ = img.shape

angle = 10 #counter clockwise positive

M = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)
img = cv2.warpAffine(img,M,(cols,rows))

cv2.imwrite('1.png',img)



