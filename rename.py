from os import walk,path
import os
from tqdm import tqdm

ext = 'png'

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

files = []

curr_folder = os.path.dirname(path.realpath(__file__))
for (dirpath, dirnames, filenames) in walk(curr_folder):
	for name in filenames:
		if (name.endswith(ext)):
			files.append(name)
	files.sort()
	for j in tqdm(range(len(files))):
		ori_dir = dirpath + '/' + files[j]
		destination=(dirpath+'/a'+'/'+str(j+1)+'.'+ext)
		ensure_dir(destination)	
		#print(ori_dir)
		os.rename(ori_dir, destination)

	files_2 = []
	for (dirpath2, dirnames, filenames) in walk(dirpath+'/a'):
		for name in filenames:
			if (name.endswith(ext)):
				files_2.append(name)
		for j in tqdm(range(len(files_2))):
			name = files_2[j]
			ori_dir=(dirpath2+'/'+name)
			destination=(dirpath+'/'+name)
			ensure_dir(destination)
			os.rename(ori_dir, destination)
		break
	os.rmdir(dirpath2)
	break
