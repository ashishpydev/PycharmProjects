def calc_fact(x):
	if x == 1:
		return 1
	else:
		return (x * calc_fact(x - 1)) # recursive function
	

print(calc_fact(5))

	

