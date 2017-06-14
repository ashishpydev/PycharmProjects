class SmallestMultiple:
	def __init__(self):
		self.smallest_val = 0
		
	def get_num(self):
		for v in range(10001):
			self.is_divisible(v)
		return self.smallest_val
			
	def is_divisible(self, v):
		count = 0
		
		for i in range(10):
			if i == 0:
				i = 1
			if v == 0:
				v = 1
			
			if v % i == 0:
				count += 1
				
		if count == 10:
			if self.smallest_val < v:
				self.smallest_val = v
		return self.smallest_val
	
SmallestMultiple = SmallestMultiple()
SmallestMulti = SmallestMultiple.get_num()
print(SmallestMulti)
