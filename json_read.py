from json import load as j_load

def read_json(filename):
	try:
		input_file = open(filename)
		json_array = j_load(input_file)
		return json_array
	except:
		return

my_dict = read_json("path to json file")

print(my_dict)
