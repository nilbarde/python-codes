import cv2

read_name = '1.png'
write_name = '2.png'

img = cv2.imread(read_name)
f_rows = 200
f_cols = 200

img = cv2.resize(img,(f_rows,f_cols))

cv2.imwrite(write_name,img)




