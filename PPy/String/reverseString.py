def guess(secret):
	reverse_str1 = secret[::-1]
	print(reverse_str1)


guess('abc dba')


def reverse(str):
	rlst = str.split(" ")
	print(' '.join(rlst[::-1]))
	
reverse("Ashish Agrawal")
