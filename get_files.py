import os

curr_folder = os.path.dirname(os.path.realpath(__file__))

ext = 'png'

folders = []

folders.append(curr_folder)

for (dirpath, dirnames, filenames) in os.walk(curr_folder):
	for fold in dirnames:
		folders.append(dirpath + '/' + fold + '/')

files = []

for folder in folders:
	for (dirpath, dirnames, filenames) in os.walk(folder):
		for name in filenames:
			if (1): #(name.endswith(ext))
				files.append(folder+name)
		break

for i in range (len(files)):
	print(files[i])














