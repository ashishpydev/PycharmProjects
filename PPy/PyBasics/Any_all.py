# Returns true if any of the items is True. It returns False if empty or all are false.
# Any can be thought of as a sequence of OR operations on the provided iterables.

# Since all are false, false is returned
print (any([False, False, False, True]))

# Since all are false, false is returned
print (all([True, True, True, True]))