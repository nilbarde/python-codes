import cv2
import numpy as np

img = cv2.imread('1.png')

pts1 = np.float32([[0,0],[200,25],[0,200],[200,175]])
pts0 = np.float32([[0,0],[200,0],[0,200],[200,200]])

M = cv2.getPerspectiveTransform(pts1,pts0)

dst = cv2.warpPerspective(img,M,(200,200))

cv2.imwrite('2.png',dst)




