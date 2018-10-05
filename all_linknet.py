import linknet
from parameters import params
from basic_augmentor import augmentor
import cv2 
import tensorflow as tf
import numpy as np
import itertools
import matplotlib.pyplot as plt
import scipy.misc
import time
import os
from argparse import ArgumentParser
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge, CvBridgeError
# import rospy

class Linknet(augmentor):
	def __init__(self):
		super(Linknet, self).__init__()
		self.model=linknet.building_block(inputs=self.inputs,classes=self.num_classes)
		self.output = tf.nn.softmax(self.model)
		self.cost=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.model[0], labels=self.semantics[0]))*0.1+tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=self.model[1], labels=self.semantics[1]))*0.9
		self.optimizer = tf.train.AdamOptimizer().minimize(self.cost)
		self.gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=1.0)
		self.Session = tf.Session()
		self.saver=tf.train.Saver()
		self.init_op= tf.initialize_all_variables()
		self.Session.run(self.init_op)

		if tf.train.latest_checkpoint(self.save_path) is not None:
			self.checkpoint=tf.train.latest_checkpoint(self.save_path)
			self.saver.restore(self.Session,self.checkpoint)
			self.load_pre_details()
			print("")
			print("")
			print("----------------------------------------------------")
			print("pre existing model found  :",self.checkpoint)
			print("----------------------------------------------------")
			print("")
			print("")
		else:
			print("")
			print("")
			print("----------------------------------------------------")
			print("no model found training from scratch")
			print("----------------------------------------------------")
			print("")
			print("")
	
	def class_indexing(self,y):
		colors = []
		y=np.vectorize(self.class_color.get, otypes=[np.float])(y)
		ground_truth = np.zeros((self.height,self.width,self.num_classes),dtype='int16')
		for i in range(self.num_classes):
			layer= y==i
			layer=layer.astype(int)
			ground_truth[:,:,i]=layer
		return ground_truth

	def image_semantics(self,condition="training"):
		if condition == "training":
			(data_dir,gt_dir)=(self.train_data,self.train_gt)
			(data_names,gt_names)=(self.train_data_names,self.train_gt_names)
			data_size=self.train_data_size
		
		elif condition == "validation":
			(data_dir,gt_dir)=(self.val_data,self.val_gt)
			(data_names,gt_names)=(self.val_data_names,self.val_gt_names)   
			data_size=self.val_data_size
			
		data = np.zeros((self.batch_size,self.height,self.width,3),dtype='uint8')
		gt = np.zeros((self.batch_size,self.height,self.width,self.num_classes),dtype='uint8')
		
		for i in range(data_size//self.batch_size):
			names=[]
			for j in range(self.batch_size):
				data[j,:,:,:] = cv2.imread(data_names[i*self.batch_size+j])
				gt_pre_img = cv2.imread(gt_names[i*self.batch_size+j],0)
				gt[j,:,:,:] = self.class_indexing(gt_pre_img)
				names.append(gt_names[i*self.batch_size+j].replace(gt_dir,""))
			if(condition == "training"):
				data,gt,names = self.augment_batch(data,gt,names)
			data = data.astype('int16')
			gt = gt.astype('int16')
			yield data,gt,names

	def compare_update(self,gt_img,pred_img):
		for class_gt in range(self.num_classes):
			self.confusion_mat[class_gt]*=self.counter_mat[class_gt]
			mask_gt = gt_img[:,:,class_gt]
			self.counter_mat[class_gt]+=np.sum(mask_gt)
			for class_pred in range(self.num_classes):
				self.confusion_mat[class_gt,class_pred]+=np.sum(pred_img[:,:,class_pred]*gt_img[:,:,class_gt])
			self.confusion_mat[class_gt,:]/=self.counter_mat[class_gt]

	def label2mask(self,output,name,image_data,mode,dump_dir="./dummy_dump",id__=1):
		# image=self.label2color_table[output.astype(int)]
		image = (output*255).astype("uint8")
		image =  cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		masked_image=self.mask_fraction*image_data+(1-self.mask_fraction)*hsv
		if(mode=='ros'):
			masked_image = masked_image.astype('uint8')
			if(id__==1):
				self.pub1.publish(self.bridge.cv2_to_imgmsg(masked_image, "bgr8"))
			elif(id__==2):
				self.pub2.publish(self.bridge.cv2_to_imgmsg(masked_image, "bgr8"))
			elif(id__==3):
				self.pub3.publish(self.bridge.cv2_to_imgmsg(masked_image, "bgr8"))
			return masked_image
		if(mode=='video'):
			return masked_image
		else:
			self.ensure_dir(dump_dir+name)
			cv2.imwrite(dump_dir+name,masked_image)
			return masked_image

	def label2image(self,output,name,mode,dump_dir="./dummy_dump"):
		#image=self.label2color_table[output.astype(int)]
		#masked_image=self.mask_fraction*image_data+(1-self.mask_fraction)*image
		image = (output*255).astype("uint8")
		image =  cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		if(mode=='ros'):
			self.wide_img[:,(self.wide_width-self.width)/2:(self.wide_width+self.width)/2,:] = hsv[:,:,:]
			self.wide_img = cv2.cvtColor(self.wide_img,cv2.COLOR_BGR2RGB)
			pil_im = Image.formarray(self.wide_img)
			pil_im = pil_im.resize((self.ipm_width,self.ipm_height))
			cv2_im = numpy.array(pil_im)
			cv2_im = cv2_im[:, :, ::-1].copy()
			image = cv2_im.astype('uint8')
			self.pub.publish(self.bridge.cv2_to_imgmsg(image, "bgr8"))
			return image
		else:
			self.ensure_dir(dump_dir+name[:-3]+"png")
			cv2.imwrite(dump_dir+name[:-3]+"png",hsv)#image)

	def validate(self):
		cost=0.0
		print("generating result images in ./val/result/")
		print("")
		val_it=self.image_semantics("validation")
		counter = 0
		for val_inputs,val_semantics,names in val_it:
			sub_cost,outputs=self.Session.run([self.cost,self.output],feed_dict={self.inputs:val_inputs,self.semantics:val_semantics})
			cost+=sub_cost
			print("valiation loss is "+str(sub_cost)+"  step :"+str(counter))
			counter+=1
			#for output,name,val_input,val_semantic in itertools.izip(output,names,val_inputs,val_semantics):
			for i in range(len(names)):
				output,name,val_input,val_semantic = outputs[i],names[i],val_inputs[i],val_semantics[i]
				self.label2mask(output=output[:,:,1],name=name,image_data=val_input,mode='validate',dump_dir=self.val_mask)
				self.label2image(output=output[:,:,1],name=name,mode='validate',dump_dir=self.val_image_dump)
				self.compare_update(gt_img=val_semantic,pred_img=output)

		print('loss is ',cost/(self.val_data_size//self.batch_size))
		self.val_losses.append(cost/(self.val_data_size//self.batch_size))
		print("")
		print(" all images have been written you can check them at ",self.val_image_dump)
		print("")
		print("-------------------------------------------------------")
	
	def save_graph_csv(self,epoch):
		plt.plot(range(epoch+1),self.train_losses,color='blue')
		plt.plot(range(epoch+1),self.val_losses,color='red')
		plt.xlabel('epoch number')
		plt.legend(('train_loss','val_loss'), loc = 'upper right')
		plt.ylabel('loss')
		plt.savefig('loss.png')
		self.ensure_dir(self.result_fold)
		np.savetxt(self.result_fold+'losses.csv',(self.train_losses,self.val_losses),delimiter=',')
		np.savetxt(self.result_fold+'confusion_matrix_'+str(epoch)+'.csv', self.confusion_mat, delimiter=",")

	def train(self):
		self.define_training_constants()
		# self.validate()
		for epoch in range(self.epochs):
			self.confusion_mat.fill(0.0)
			self.counter_mat.fill(0.0)
			train_it=self.image_semantics("training")
			counter=0.0
			epoch_loss = 0.0
			print('epoch:'+str(epoch+1)+'/'+str(self.epochs))
			for epoch_x,epoch_y,names in train_it:#num_images//batch_size):
				counter+=1.0
				_, c = self.Session.run([self.optimizer, self.cost], feed_dict={self.inputs: epoch_x, self.semantics: epoch_y})
				print("loss is "+str(c)+"  step :"+str(counter))
				epoch_loss+=c
			epoch_loss/=counter	
			self.train_losses.append(epoch_loss)
			save_path = self.saver.save(self.Session,self.save_path+"model"+str(self.init_epochs + epoch)+".ckpt")
			print("Model saved in path: %s" % self.save_path)
			print("################### validating ##################")
			print("----------  this may take some time --------------")
			self.validate()
			self.save_graph_csv(epoch)

	def crop_resize(self,img):
		h,w,_ = img.shape
		if (h==self.height and w==self.width):
			return img
		c_h,c_w = w / self.aspect_ratio, h * self.aspect_ratio
		if(c_w<w):
			img = img [:,(int(w-c_w)/2):int((w+c_w)/2)]
		elif(c_h<h):
			img = img [(h-c_h)/2:(h+c_h)/2,:]
		if(self.height == img.shape[0]):
			return img
		else:
			img = cv2.resize(img,(self.width,self.height))
			return img

	########################### ROS integration ###########################
	def image_retreive(self,img):
		try:
			# Convert your ROS Image message to OpenCV2
			img = self.bridge.imgmsg_to_cv2(img, "bgr8")
			img = self.crop_resize(img)
			#self.find_road(img)
			output=self.Session.run(self.output,feed_dict={self.inputs:img.reshape(-1,self.height,self.width,3).astype('int16')})
			self.label2mask(output=output[:,:,1],name='a.png',image_data=img,mode='ros',id__=1)
			self.label2image(output=output[:,:,1],name='a.png',mode='ros')
		except CvBridgeError as e:
			print(e)

	def ros_run(self,chn_list):
		self.define_testros_constants()
		while not rospy.is_shutdown():
			if chn_list is None:
				chn_list = self.default_channels
			# for chn in chn_list:
			rospy.Subscriber("/camera2/image_raw",Image,self.image_retreive)
			self.rate.sleep()
		rospy.spin()

	########################### testing folder ############################
	def test_folder(self,folders):
		self.define_testimage_constants()
		print("**********************************111111111111111")
		if folders is None:
			folders = self.get_folders(self.test_data)
		print(folders)
		self.test_img_list = self.get_files(folders,".jpg")#self.data_image_format)
		print(self.test_img_list)
		self.test_data_size = len(self.test_img_list)
		self.test_batch_size = 2 # = self.batch_size
		self.test_image_dimension = (self.test_batch_size,self.height,self.width,3)
		self.test()

	def get_test_data(self):
		data = np.zeros(self.test_image_dimension,dtype='uint8')
		names = []
		for i in range(self.test_data_size//self.test_batch_size):
			names = []
			for j in range(self.test_batch_size):
				data[j,:,:,:] = self.crop_resize(cv2.imread(self.test_img_list[i*self.test_batch_size+j]))
				names.append(self.test_img_list[i*self.test_batch_size+j][len(self.test_data):])
			print(names)
			data.astype('int16')
			yield data,names

	def test(self):
		val_it=self.get_test_data()
		for val_inputs,names in val_it:
			outputs=self.Session.run(self.output,feed_dict={self.inputs:val_inputs})
			# for output,name,val_input in itertools.izip(outputs,names,val_inputs):
			for i in range(len(outputs)):
				output,name,val_input = outputs[i],names[i],val_inputs[i]
				self.label2mask(output[:,:,1],image_data=val_input,name=name,mode='test',dump_dir=self.test_mask) 
				self.label2image(output[:,:,1],name=name,mode='test',dump_dir=self.test_result) 
				# what is the dump directory and  where is it specified?
				# parameters.py self.test_mask
				
	########################### testing video #############################
	def test_video(self,filenames):
		self.define_testvideo_constants()
		if filenames is None:
			filenames = [self.test_video]
		for filename in filenames:
			video = cv2.VideoWriter(self.test_videos+filename,self.fourcc,10,(self.width,self.height),True)
			vidcap = cv2.VideoCapture(filename)
			success,image = vidcap.read()
			while success:
				success,img = vidcap.read()
				img = self.crop_resize(img)
				output=self.Session.run(self.output,feed_dict={self.inputs:img.reshape(-1,self.height,self.width,3).astype('int16')})
				image = self.label2mask(output[:,:,1],filename,image_data,'video',self.test_mask)
				video.write(image)
			video.release()
	#######################################################################

parser = ArgumentParser()
parser.add_argument("-m", "--mode", dest="action",default='train')
parser.add_argument("-c", "--channels",nargs = '+' ,dest="channels")
parser.add_argument("-f", "--folders",nargs = '+' ,dest="folders")
parser.add_argument("-v", "--videos",nargs = '+' ,dest="videos")

args = parser.parse_args()

link=Linknet()
if(args.action=='train'):
	link.train()

elif(args.action=='validate'):
	link.validate()

elif(args.action=='test_ros'):
	link.ros_run(args.channels)

elif(args.action=='test_videos'):
	link.test_videos(args.videos)

elif(args.action=='test_images'):
	link.test_folder(args.folders)

else:
	print('modes available are train , validate , test_ros , test_videos , test_images')



	
