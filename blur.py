import cv2
import numpy as np

read_name = '1.png'
write_name = '2.png'

img = cv2.imread(read_name)

level = 5

#2d blur
kernel = np.ones((level,level),np.float32)/(level*level)
img = cv2.filter2D(img,-1,kernel)

#gaussian blur
#img = cv2.GaussianBlur(img,(level,level),0)

#median blur
#img = cv2.medianBlur(img,level)

cv2.imwrite(write_name,img)








