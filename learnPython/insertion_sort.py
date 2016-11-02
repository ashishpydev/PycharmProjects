def bubble_sort(lst):
	for i in range(0, len(lst)):
		sorted_num = lst[i]
		for j in range(i+1, len(lst)):
			if current_num > lst[j]:
				lst[i], lst[j] = lst[j], lst[i]
			elif current_num < lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]
		return lst
	
lst = [4, 2, 8, 3, 1]
print(bubble_sort(lst))
