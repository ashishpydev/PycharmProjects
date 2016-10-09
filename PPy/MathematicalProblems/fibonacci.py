def fib(n):
	a, b = 0, 1
	fibs = []
	while a < n:
		fibs.append(a)
		a, b = b, a + b
	return fibs
		
print(fib(10))
