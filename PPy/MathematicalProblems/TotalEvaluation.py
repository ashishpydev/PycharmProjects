def eval(lst):
	count = 0
	for i in range(len(lst)):
		if sum(lst[:i]) ==sum(lst[i:]):
			print("It is equal Sum")
			count += 1
			yield(i)
		else:
			yield -1
	if(count == 0):
		yield -1

y = eval([1, 2, -2, 1])
print(next(y))
print(next(y))
print(next(y))
print(next(y))
