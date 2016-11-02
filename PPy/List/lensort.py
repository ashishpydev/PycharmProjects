# Write a function lensort to sort a list of strings based on length.


def lensort(lst):
	for i in range(0, len(lst) - 1):
		for j in range(0, len(lst) - i -1):
			if len(lst[j]) > len(lst[j+1]):
				lst[j], lst[j+1] = lst[j+1], lst[j]
	print(lst)
				
l = ['python', 'per', 'ja', 'c', 'haskell', 'ruby']
lensort(l)

