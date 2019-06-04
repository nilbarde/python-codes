from codecs import open as co_open

from json import dump as j_dump
from json import load as j_load

from os.path import dirname as os_dirname
from os.path import exists as os_exists
from os import makedirs as os_makedirs

def read_json(filename):
	input_file = open(filename)
	json_array = j_load(input_file)
	return json_array

def ensure_dir(file_path):
	if '/' in file_path:
		directory = os_dirname(file_path)
		if not os_exists(directory):
			os_makedirs(directory)

def write_json(dict_,file_path):
	ensure_dir(file_path)
	j_dump(dict_, co_open(file_path, 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)

