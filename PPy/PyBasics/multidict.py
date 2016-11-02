from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

s = defaultdict(set)
s['a'].add(1)
s['a'].add(2)
s['b'].add(4)
print(s)

# One caution with defaultdict is that it will automatically create dictionary entries for keys accessed later on
# (even if they aren’t currently found in the dictionary). If you don’t want this behavior,
#  you might use setdefault() on an ordinary dictionary instead.
r = {}  # A regular dictionary
r.setdefault('a', []).append(1)
r.setdefault('a', []).append(2)
r.setdefault('b', []).append(4)
print(r)
