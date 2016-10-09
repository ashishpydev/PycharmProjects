# when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate it with.
#  We can get the address (in RAM) of some object through the built-in function, id(). Let's check it.

a = 2
print id(2)
print id(a)
a += 1
print id(3)

b = 2
print id(2)
print id(b)