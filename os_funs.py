from os import walk, listdir, stat, makedirs
from os.path import exists, getsize, isfile, getmtime, getctime, splitext, dirname
from time import ctime
from datetime import datetime
import subprocess

def get_folders(curr_folder,deep=False,address=False):
	folders_com = []
	for (dirpath, dirnames, filenames) in walk(curr_folder):
		folders = []
		if(address):
			for fold in dirnames:
				name = dirpath + '/' + fold + '/'
				name = name.replace("//","/")
				folders.append(name)
		else:
			folders = dirnames
		folders.sort()
		folders_com = folders_com + folders
		if not deep:
			break
	return folders_com

def get_files(folder,exts=None,address=False):
	# files_fold = ([(i) for i in listdir(folder) if ("." in i)])
	files_fold = []
	for (dirpath, dirnames, filenames) in walk(folder):
		files_fold = filenames
		break
	files_fold.sort()
	files_ext = []
	if not (exts is None):
		if(type("s")==type(exts)):
			exts = [exts]
		for filename in files_fold:
			for ext in exts:
				if(filename.endswith(ext)):
					files_ext.append(filename)
	if(exts is None):
		files_ext = files_fold
	files = []
	for filename in files_ext:
		name = ''
		if(address):
			name += folder + "/"
		name += filename
		name = name.replace("//","/")
		files.append(name)
	return files

def ensure_dir(file_path):
	if '/' in file_path:
		directory = dirname(file_path)
		if not exists(directory):
			makedirs(directory)

def get_size(file_path="."):
	size_ = (subprocess.check_output(['du','-sh', file_path.replace("//","/")]).split()[0])
	return str(size_),file_path

def get_modified_time(file_path):
	ttt = getmtime(file_path)
	edited = str(datetime.fromtimestamp(int(ttt)))
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	if(edited[:-9]==now[:-9]):
		return(edited[-8:-3])
	else:
		if(edited[:4]==now[:4]):
			return(edited[5:-9])
		else:
			return(edited[:4])

def get_modified_date(file_path):
	ttt = getmtime(file_path)
	edited = str(datetime.fromtimestamp(int(ttt)))
	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	return(edited[:-9])
