
def selection_sort(lst):
	for i in range(0, len(lst) -1):
		min = i
		for j in range(i+1, len(lst)):
			if lst[j] < lst[min]:
				min = j
			if min != i:
				lst[i], lst[min] = lst[min], lst[i]
	return lst
			
		
lst = [4, 2, 8, 3, 1]
print(selection_sort(lst))