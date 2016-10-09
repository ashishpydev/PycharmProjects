	
	
	# Multiply values from start range : 100 to end Range: 999
	# Multiple by looping through start_range to start_range + 1
	# For each result of multiplication I will pass it to the function is palindrome
	# If the value is palindrome I will pass it to function find_highest which will
	#  have a value for the last highest value and compare it.
	
class LargestPalindrome:
	def __init__(self):
		self.highest_val = 0
		
	def get_products(self):
		for i in range(100, 1000):
			for j in range(100, 1000):
				prod = i * j
				print("Product of values i {} and j {} is {}".format(i, j, prod))
				self.is_palindrome(prod)
		return self.highest_val
			
	def is_palindrome(self, prod):
		pr = str(prod)
		pr = (pr[::-1])
		rev_prod = int(pr)
		if prod == rev_prod:
			self.find_highest(prod)
		else:
			print("Value {} is not palindrome.".format(prod))
		
	def find_highest(self, palindrome):
		if palindrome > self.highest_val:
			self.highest_val = palindrome
		else:
			print("Value {} is not Highest.".format(palindrome))
		
		return self.highest_val
		

LargestPalindrome = LargestPalindrome()
hig_val = LargestPalindrome.get_products()
print("Highest Value {} of Palindrome of Multiplication.".format(hig_val))

