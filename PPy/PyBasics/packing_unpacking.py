# Consider a situation where we have a function that receives four arguments.
#  We want to make call to this function and we have a list of size 4 with us that
# has all arguments for the function. If we simply pass list to the function,


# A Python program to demonstrate need
# of packing and unpacking

# A sample function that takes 4 arguments
# and prints them.
# Packing Example


def fun1(a, b, c):
	print(a, b, c)


# Driver Code
# my_list = [1, 2, 3]

# This doesn't work
# fun1(*my_list)
#

# Unpacking Example
def fun2(*args):
	args = list(args)
	fun1(*args)
	
fun2('Hello', 'beautiful', 'world!')
