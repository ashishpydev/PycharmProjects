import numpy


def get_fib(n):
	fib = []
	a, b = 0, 1
	sum = 0
	while a < n:
		if a % 2 == 0:
			fib.append(a)
		a, b = b, a+b
	return numpy.sum(fib)

print(get_fib(4000000))
