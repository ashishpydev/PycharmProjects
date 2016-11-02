def insertion_sort(A):
	for i in range(1, len(A)):
		cur_num = A[i]
		print("Current Number is: {}".format(cur_num))
		for j in range(i-1, -1):
			print("A[j] is: {}".format(A[j]))
			if A[j] > cur_num:
				print("A[j+1] is: {}".format(A[j+1]))
				A[j+1] = A[j]
			else:
				A[j + 1] = cur_num
				break
			print("Updated List: {}".format(A))
	print(A)

insertion_sort([10, 9, 24, 6, 56])
