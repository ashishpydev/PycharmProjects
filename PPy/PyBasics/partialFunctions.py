# Partial functions allow us to fix a certain number of arguments of a function and generate a new function.

from functools import partial

# Example1:

#
# def f(a, b, c, x):
# 	return 1000 * a + 100 * b + 10 * c + x
#
# # A partial function that calls f with
# # a as 3, b as 1 and c as 4.
# g = partial(f, 3, 1, 4)
#
# # Calling g()
# print(g(5))

# Example 2:


def sum(a, b, c):
	sum = a*100 + b*10 + c*10
	print(sum)
getsum = partial(sum, b=5, c=6)
getsum(2)
