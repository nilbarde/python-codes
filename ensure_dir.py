from os.path import dirname as os_dirname
from os.path import exists as os_exists
from os import makedirs as os_makedirs

def ensure_dir(file_path):
	if '/' in file_path:
		directory = os_dirname(file_path)
		if not os_exists(directory):
			os_makedirs(directory)

