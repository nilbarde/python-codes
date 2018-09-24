from codecs import open as co_open
from json import dump as j_dump
from os.path import dirname as os_dirname
from os.path import exists as os_exists
from os import makedirs as os_makedirs

def ensure_dir(file_path):
	if '/' in file_path:
		directory = os_dirname(file_path)
		if not os_exists(directory):
			os_makedirs(directory)

def write_json(file_path,my_dict):
	ensure_dir(file_path)
	j_dump(my_dict, co_open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True)#, indent=4)

my_dict = {}

write_json('./new.json',my_dict)
