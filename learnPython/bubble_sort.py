def bubble_sort(lst):
	for i in range(0, len(lst) - 1):
		for j in range(len(lst) - i - 1):
			if lst[j]> lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
		
	return lst

lst = [4, 2, 8, 3, 1]
print(bubble_sort(lst))

