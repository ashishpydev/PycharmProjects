from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

print(OrderedDict(d))
print(OrderedDict(sorted(d.items())))
# dictionary sorted by key
print(OrderedDict(sorted(d.items(), key = lambda x : x[0])))
# dictionary sorted by value
print(OrderedDict(sorted(d.items(), key = lambda x : x[1])))
# dictionary sorted by length of the key string
print(OrderedDict(sorted(d.items(), key = lambda x : len(x[0]))))
