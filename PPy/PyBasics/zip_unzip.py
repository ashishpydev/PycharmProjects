# This function is helpful to combine similar type iterators(list-list or dict- dict etc)
# data items at ith position. It uses shortest length of these input iterators.
# Other items of larger length iterators are skipped. In case of empty iterators it returns No output.

cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit", "Dolby sound kit", "mount"]
bike = ["Bajaj", "RE", "Honda"]

# Combining lists and printing
ca = zip(cars, accessories, bike)
print("Zipped List: {}".format(ca))
	
# The reverse of getting iterators from zip function is known as
#  unzipping using "*" operator.
# Python program to demonstrate unzip (reverse
# of zip)using * with zip function

# Unzip lists
cars, accessories, bike = zip(*ca)
# Printing unzipped lists
print("UnZipped List cars: {}".format(cars))
print("UnZipped List accessories: {}".format(accessories))
