

def find_multiples(val):
	rsum = 0
	for i in range(val):
		if(i % 3 == 0 or i % 5 == 0):
			rsum += i
	return rsum
	
			
print(find_multiples(1000))
