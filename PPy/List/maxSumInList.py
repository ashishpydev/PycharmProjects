def max_sum(l):
	best = cur = 0
	for i in l:
		cur = max(cur + i, 0)
		best = max(best, cur)
	return best
	
lmst = [-1, -2, 3, 4, -5, 6]
print(max_sum(lmst))
