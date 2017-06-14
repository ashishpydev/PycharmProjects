lst = [3, 4, 5, 6]
# The function is called with all the items in the list
# and a new list is returned which contains items for which the function evaluats to True.
print (list(filter(lambda x: (x % 2), lst)))
print (list(filter(lambda x: (x % 2 == 0), lst)))

# The function is called with all the items in the list and a new list is returned which
#  contains items returned by that function for each item.
print (list(map(lambda x: (x % 2 == 0), lst)))
print (list(map(lambda x: (x % 2), lst)))
print (list(map(lambda x: (x * 2), lst)))
print (list(map(lambda x: (x + 2), lst)))
