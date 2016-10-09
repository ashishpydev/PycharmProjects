def square_of_first_one_hundred(val):
	sq_sum = 0
	for i in range(val + 1):
		sq = i*i
		sq_sum += sq
	return sq_sum


def sum_of_square(val):
	sum_sq = 0
	for i in range(val + 1):
		sum_sq += i
	sum_sq = sum_sq * sum_sq
	return sum_sq

val = 100
sq_sum = square_of_first_one_hundred(val)
sum_sq = sum_of_square(val)
print(sq_sum)
print(sum_sq)
diff = sum_sq - sq_sum
print(diff)

