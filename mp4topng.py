import cv2

now = i
fps = 60
count = 0
vidcap = cv2.VideoCapture('1.mp4')
success,image = vidcap.read()
success = True

while success:
	print(count)
	success,image = vidcap.read()
	if(image!=None and count%fps==0):
		cv2.imwrite("images/"+str(count/fps)+".png", image)     # save frame as JPEG file
	if cv2.waitKey(10) == 27:                # exit if Escape is hit
		break
	count += 1






