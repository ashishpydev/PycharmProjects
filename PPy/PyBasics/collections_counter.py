from collections import Counter

dict_count = Counter()
lst_count = Counter()
dict = {1: 'red', 2: 'blue', 3: 'black', 4: 'red', 5: 'blue', 6: 'black'}
lst = ['red', 'blue', 'black', 'red', 'blue', 'black']

for color in dict.values():
	dict_count[color] += 1
	
print(dict_count)

for color in lst:
	lst_count[color] += 1

print(lst_count)