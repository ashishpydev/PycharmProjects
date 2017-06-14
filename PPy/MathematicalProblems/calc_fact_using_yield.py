def calc_fact(n):
	fact = 1
	for i in range(1, n+1):
		fact = fact * i
		yield fact

mygen = calc_fact(10)
for i in mygen:
	print(i)