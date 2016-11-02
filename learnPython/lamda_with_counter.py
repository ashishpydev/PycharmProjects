from collections import Counter, OrderedDict

lst = [2, 3, 4, 2, 4, 5]

print(Counter(lst))
count = Counter()
ls = ['blue', 'green', 'black', 'blue', 'green']
for color in ls:
	count[color] += 1
print count


# Ordered Dict

dict = {2: 'ABC', 1: 'DEF', 4: 'GHI', 3: 'JKL'}

sDict = OrderedDict(sorted(dict.items()))
print(sDict)
sDict_key = OrderedDict(sorted(dict.items(), key=lambda x: x[0]))
print(sDict_key)
sDict_val = OrderedDict(sorted(dict.items(), key=lambda x: x[1]))
print(sDict_val)