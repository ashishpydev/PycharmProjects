# Given a set of non-negative integers, and a value sum, determine if
# there is a subset of the given set with sum equal to given sum.


# Check if there is any element more than
#  the value of given sum. If there is any value above it pop it.

# #
# def is_subset_sum(st, sm):
# 	l = len(st)
# 	print(l)
# 	for ind, val in enumerate(st):
# 		for vl in range(l):
# 			if vl != l:
# 				v = st[vl + 1]
# 				if sm == val + v:
# 					print("Found sum {} during iteration of {} plus {}".format(sm, val, v))
# 					break
			
if __name__ == '__main__':
	i_set = {3, 34, 4, 12, 5, 2}
	lst = list(i_set)
	i_sum = 9
	st = list(filter(lambda x: x > i_sum, lst))
	print(st)
	# print(is_subset_sum(st, i_sum))
