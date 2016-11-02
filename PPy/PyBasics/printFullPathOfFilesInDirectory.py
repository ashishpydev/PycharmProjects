import os


def get_full_path():
	dir = "/Users/ashishagrawal/PycharmProjects/PPy/BST"
	ls = os.listdir(dir)
	for f in ls:
		print(dir + "/" + f)
	
get_full_path()
