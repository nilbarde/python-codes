from cv2 import imread, imwrite, imshow, waitKey, resize, add, multiply, cvtColor, COLOR_BGR2RGB, destroyAllWindows, Canny, flip, getPerspectiveTransform, warpPerspective
from numpy import zeros, array, float32
from PIL.Image import fromarray, open, FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM

def image_crop(img,u_row=-1,l_row=-1,l_col=-1,r_col=-1):
	my_shape = img.shape
	if(u_row==-1):
		u_row = 0
	elif(0<u_row<1.0):
		u_row = int(my_shape[0]*u_row)
	if(l_row==-1 or l_row==0):
		l_row = my_shape[0]
	elif(0<l_row<1.0):
		l_row = int(my_shape[0]*l_row)
	if(l_col==-1):
		l_col = 0
	elif(0<l_col<1.0):
		l_col = int(my_shape[1]*l_col)
	if(r_col==-1 or r_col==0):
		r_col = my_shape[1]
	elif(0<r_col<1.0):
		r_col = int(my_shape[1]*r_col)
	new_img = img[u_row:l_row,l_col:r_col]

	return new_img

def image_resize(img,f_rows=-1,f_cols=-1):
	my_shape = img.shape
	if(f_rows==-1 or f_rows==0):
		f_rows = my_shape[0]
	elif(f_rows!=int(f_rows)):
		f_rows = int(my_shape[0]*f_rows)
	if(f_cols==-1 or f_cols==0):
		f_cols = my_shape[1]
	elif(f_cols!=int(f_cols)):
		f_cols = int(my_shape[1]*f_cols)
	new_img = resize(img,(f_cols,f_rows))

	return new_img

def image_contrast(img,alpha=1,beta=0):
	array_alpha = array([alpha]).astype(float)
	array_beta = array([beta]).astype(float)
	add(img, array_beta, img)
	multiply(img, array_alpha, img)

	return img

def cv2_pil(img):
	img = cvtColor(img,COLOR_BGR2RGB)
	pil_im = fromarray(img)

	return pil_im

def image_edges(img,l_bound=0,u_bound=100):
	edges = Canny(img,l_bound,u_bound)
	return edges

def image_flip(img,axis=None):
	if(axis==None):
		return img
	elif(axis=="h" or axis=="hor" or axis=="horizontal"):
		axis = 1
	elif(axis=="v" or axis=="ver" or axis=="vertical"):
		axis = 0
	elif(axis=="r" or axis=="rot" or axis=="rotate" or axis=="rotate180" or axis==180):
		axis = -1
	if(axis==0 or axis==1 or axis==-1):
		print(type(img))
		if(str(type(img))=="<type 'numpy.ndarray'>"):
			new_img = flip(img,axis)
			return new_img
		elif(str(type(img))=="<class 'PIL.Image.Image'>"):
			if(axis==0):
				new_img = img.transpose( FLIP_TOP_BOTTOM )
				return new_img
			elif(axis==1):
				new_img = img.transpose( FLIP_LEFT_RIGHT )
				return new_img
	return img

def image_view(img,p_u_l=[-1,-1],p_u_r=[-1,-1],p_d_l=[-1,-1],p_d_r=[-1,-1],f_rows=-1,f_cols=-1):
	my_shape = img.shape
	print(p_u_l)
	if(p_u_l[0]==-1):
		p_u_l[0]=0
	elif(0.0<=p_u_l[0]<=1.0):
		p_u_l[0]*=my_shape[0]
	if(p_u_l[1]==-1):
		p_u_l[1]=0
	elif(0.0<=p_u_l[1]<=1.0):
		p_u_l[1]*=my_shape[1]

	if(p_u_r[0]==-1):
		p_u_r[0]=0
	elif(0.0<=p_u_r[0]<=1.0):
		p_u_r[0]*=my_shape[0]
	if(p_u_r[1]==-1 or p_u_r[1]==0):
		p_u_r[1]=my_shape[1]
	elif(0.0<=p_u_r[1]<=1.0):
		p_u_r[1]*=my_shape[1]

	if(p_d_l[0]==-1 or p_d_l[0]==0):
		p_d_l[0]=my_shape[0]
	elif(0.0<=p_d_l[0]<=1.0):
		p_d_l[0]*=my_shape[0]
	if(p_d_l[1]==-1 or p_d_l[1]==0):
		p_d_l[1]=0
	elif(0.0<=p_d_l[1]<=1.0):
		p_d_l[1]*=my_shape[1]

	if(p_d_r[0]==-1 or p_d_r[0]==0):
		p_d_r[0]=my_shape[0]
	elif(0.0<=p_d_r[0]<=1.0):
		p_d_r[0]*=my_shape[0]
	if(p_d_r[1]==-1 or p_d_r[1]==0):
		p_d_r[1]=my_shape[1]
	elif(0.0<=p_d_r[1]<=1.0):
		p_d_r[1]*=my_shape[1]

	if(f_rows==-1 or f_rows==0):
		f_rows = my_shape[0]
	elif(f_rows!=int(f_rows)):
		f_rows = int(my_shape[0]*f_rows)
	if(f_cols==-1 or f_cols==0):
		f_cols = my_shape[1]
	elif(f_cols!=int(f_cols)):
		f_cols = int(my_shape[1]*f_cols)

	print([p_u_l,p_d_l,p_u_r,p_d_l],f_rows,f_cols)
	cut_pts = float32([p_u_l,p_d_l,p_u_r,p_d_r])
	end_pts = float32([[0,0],[f_rows,0],[0,f_cols],[f_rows,f_cols]])

	trans_mat = getPerspectiveTransform(cut_pts,end_pts)
	new_img = warpPerspective(img,trans_mat,(f_cols,f_rows))

	return new_img

# img = imread("me.jpg")
img = zeros((256,256),dtype="uint8")
imshow("img",img)

new_img = image_view(img,p_d_l=[700,100])
imshow("new_img",new_img)
#new_img.show()

waitKey(0)
destroyAllWindows()
