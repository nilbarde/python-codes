import os
import tensorflow as tf
import time
import numpy as np
from collections import defaultdict
import cv2


class params(object):
	def __init__(self):
		self.build_essential_constants()

	def build_essential_constants(self):
		self.num_classes = 2
		self.mask_fraction = 0.75
		self.gt_image_format = '.png'
		self.data_image_format = '.jpg'
		self.height = 576
		self.width = 768
		self.aspect_ratio = float(self.width)/self.height
		self.img_channels = 3
		self.ch_colors = 255.0
		self.batch_size = 1
		self.inputs=tf.placeholder(tf.float32, shape=[None, self.height, self.width, 3])
		self.semantics = tf.placeholder(tf.float32, shape=[None, self.height, self.width, self.num_classes])

		self.save_path="./model_files/"
		self.label2color_table=np.array([[0,0,0],[0,0,255]])#,[0,255,0]]) #  import another json file or a csv preferably csv 

	def define_training_constants(self):
		self.train_data = './train/data/'
		self.train_gt = './train/gt/'
		self.val_data = './val/data/'
		self.val_gt = './val/gt/'
		self.val_image_dump="./val/result/"
		self.val_mask='./val/mask/'
		self.result_fold = './result/'

		self.ensure_dir(self.save_path)
		self.ensure_dir(self.result_fold)

		self.epochs = 20

		print("")
		print("")
		print("----------------------------------processign dirpaths----------------------------------------- ")
		print("the training data will be taken from ",self.train_data,"and ground truths from ",self.train_gt)
		print("the validation data will be take from ",self.val_data,"and ground truths from ",self.val_gt)
		print("please make sure the above directories are correct")
		print("----------------------------------------------------------------------------------------------")
		
		self.init_epochs = 0 
		self.train_losses = []
		self.val_losses = []
		self.train_data_names = []
		self.train_gt_names = []
		self.val_data_names = []
		self.val_gt_names = []
		self.class_color={0:0,1:0,2:1,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:1,14:0,16:0,17:0,18:0} # import a json file later 
		self.confusion_mat = np.zeros((self.num_classes,self.num_classes))
		self.counter_mat = np.zeros((self.num_classes))

		self.train_data_names,self.train_gt_names = self.get_learning_data('training')
		self.val_data_names,self.val_gt_names = self.get_learning_data('validation')
		print("-----------------------------------------------------------------------------------------------")
		print("")
		print("")
		self.train_data_size = len(self.train_gt_names)
		print(self.train_data_size,'train data size')
		print("")
		time.sleep(0.1)
		print("")
		print("")
		self.val_data_size = len(self.val_gt_names)
		print(self.val_data_size,'val data size')
		print("---------------------------------------------------------------------------------------------")

	def define_testimage_constants(self):
		self.test_data = './test/data/'
		self.test_mask = './test/mask/'
		self.test_result = './test/result/'

	def define_testvideo_constants(self):
		self.test_videos = './test/videos/'
		self.format = "XVID"
		self.fourcc = cv2.VideoWriter_fourcc(*(self.format))
		
	def define_testros_constants(self):
		self.default_channels = ['/camera2/image_raw']
		self.bridge = CvBridge()
		self.pub1 = rospy.Publisher('/camera/linknetroad', Image,queue_size=10)
		rospy.init_node('image_listener',anonymous=True)
		self.rate = rospy.Rate(0.0000001)	
 		
	def get_learning_data(self,args):
		if(args == 'training'):
			gt_fold = self.train_gt
			data_fold = self.train_data
		elif(args == 'validation'):
			gt_fold = self.val_gt
			data_fold = self.val_data
		else:
			print('######################################')
			print('###### error in argument passed ######')
			print('######################################')
			return

		folders = self.get_folders(gt_fold)
		names = self.get_files(folders,self.gt_image_format)
		gt_names = []
		data_names = []
		print("---------------------------------------")
		print("checking data and gt images consistency")
		print("---------------------------------------")
		
		for name in names:
			
			data_name = data_fold + name[len(gt_fold):-(len(self.gt_image_format))] + self.data_image_format
			gt_names.append(name)
			data_names.append(data_name)
		return data_names,gt_names

	def count_data(self,args="training"):
		if args == "training":
			directory1=self.train_data
			directory2=self.train_gt
		elif args == "validation":
			directory1=self.val_data
			directory2=self.val_gt

		files_data = [i for i in os.listdir(directory1) if i.endswith(".jpg")]
		files_gt = [i for i in os.listdir(directory2) if i.endswith(".png")]
		if len(files_gt)==len(files_data):
			print("the count of images in GT and data are consistent")
			return len(files_gt)
		else: 	  
			print("the count of images in GT and data are NOT consistent")
			if len(files_gt)<len(files_data):
				print("gt has lower images hence using it ")
				return len(files_gt)
			else: 
				print("data has lower images hence using it ")
				return len(files_data) 
	def load_pre_details(self):
		self.init_epochs = int(self.checkpoint[19:-5])+1
	
	def get_folders(self,root_folder):
		folders = []
		folders.append(root_folder)
		for (dirpath, dirnames, filenames) in os.walk(root_folder):
			for fold in dirnames:
				folders.append(dirpath + '/' + fold + '/')
		return(folders)

	def get_files(self,folders,ext):
		files = []
		for folder in folders:
			files_fold = ([(folder+i) for i in os.listdir(folder) if i.endswith(ext)])
			files_fold.sort()
			for filename in files_fold:
				files.append(filename)
		return(files)

	def ensure_dir(self,file_path):
		directory = os.path.dirname(file_path)
		if not os.path.exists(directory):
			os.makedirs(directory)
