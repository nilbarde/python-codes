import cv2

read_name = '1.png'
write_name = '2.png'

img = cv2.imread(read_name)

l_rows = 50
u_cols = 50
r_rows = 150
d_cols = 150

img1 = img[l_rows:r_rows,u_cols:d_cols]

cv2.imwrite(write_name,img1)













