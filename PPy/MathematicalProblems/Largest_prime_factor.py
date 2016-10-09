def largest_prime(n):
	largest = 0
	for x in range(n+1):
		try:
			if n % x == 0:
				if x > largest:
					largest = x
		except:
			x = 1
			if n % x == 0:
				if x > largest:
					largest = x
			else:
				largest_prime(n)
	return largest

print(largest_prime(365))
