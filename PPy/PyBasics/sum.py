import math
#
#

#
# def add_numbers(start, end):
# 	total = 0
# 	i = start
# 	while start < end:
# 		total += i
# 		i += 1
# 		start += 1
# 	print(total)
#
# add_numbers(2, 4)
#
# # Define Lamda func
# n_list = [1, 2, 3, 4, 5]

# map: The map() function applies a function to every member of iterable and returns the result.
#  If there are multiple arguments, map() returns a list consisting of tuples containing the corresponding
#  items from all iterables.
# map = list(map(lambda x: int((math.pow(x, 2))), n_list))

# It takes a function returning True or False and applies it to a sequence, returning a
#  list of only those members of the sequence for which the function returned True.
# filter = list(filter(lambda x: int((math.pow(x, 2))), n_list))
# print(map)
# print(filter)
#


# Define Closures
# def print_msg(msg):
#     """This is the outer enclosing function"""
#
#     def printer():
#         """This is the nested function"""
#         print(msg)
#     return printer
#
# raw_inp = print_msg("hello")
# raw_inp()


# Define Decorators
# def decorated(fun):
#     print("I'm still Ordinary")
#
#     def now_inner_decorated():
#         print("Now I'm Decorated Fun")
#     return now_inner_decorated()
#
#
# @decorated
# def ordinary_fn():
#     print("I'm Ordinary Fun")
    
# The same way we call it below
# decorated(ordinary_fn())


# output
# lis = ['a', 'b', 'c', 'd', 'e']
# print lis[2:]
#
# class C:
#     dan = 3
#
# c1 = C()
# c2 = C()
# print c1.dan
#
# c1.dan = 3
# print c1.dan
# print c2.dan
#
# del c1.dan
# print c1.dan
#
# C.dan = 3
# print c2.dan


# def im_decorated(fn):
# 	print("I'm Decorated Now.")
# 	return fn
#
#
# @im_decorated
# def im_normal():
# 	print("I'm Normal Function.")
#
# im = im_normal()
