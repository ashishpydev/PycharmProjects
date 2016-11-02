def product_lst(lst):
	prod = 1
	for v in lst:
		prod *= v
	print(prod)
l = [1, 2, 3]
product_lst(l)
print(l[::-1])
