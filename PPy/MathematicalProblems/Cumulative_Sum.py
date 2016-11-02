import itertools
def cumulative_sum(lst):
	su = 0
	for i in lst:
		su += i
		yield su
		
print (list(cumulative_sum([1, 2, 3, 4])))
