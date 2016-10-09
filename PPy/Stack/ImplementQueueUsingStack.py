class Stack():
	def __init__(self):
		self.items = []
	
	def push(self, item):
		self.items.append(item)
		print("Updated The Item in stack with{}".format(self.items))
	
	def pop(self):
		item = self.items.pop()
		print("Updated stack post POP Operation {}".format(self.items))
		return item
	
	def peek(self):
		item = self.items.pop(0)
		self.items.append(item)
		return item
	
	def is_empty(self):
		if len(self.items) == 0:
			return True
		else:
			return False
	
	def stack_size(self):
		return len(self.items)


# To implement Queue using Stack
# We need to have two stacks.
# When pop operation is initiated we need to pop each item from stack1 and append it in stack2
# and pop the item from stack2 which will behave like FIFO i.e Queue

s1 = Stack()
s2 = Stack()


def pop_item():
	if s2.is_empty() is True:
		for s in s1.items[::-1]:
			s1.pop()
			s2.push(s)
		s2.pop()
	else:
		s2.pop()
	
		
s1.push(4)
s1.push(5)
s1.push(6)
s1.push(7)
pop_item()
print(s1.items)
print(s2.items)



