def insertion_sort(A):
	for i in range(1, len(A)):
		cur_num = A[i]
		for j in range(i-1, -1, -1):
			if A[j] > cur_num:
				A[j+1] = A[j]
			else:
				A[j + 1] = cur_num
				break
	print(A)

insertion_sort([4, 9, 24, 6, 56])
