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
		item = self.items.pop()
		self.items.append(item)
		return item
	
	def is_empty(self):
		if len(self.items) == 0:
			return True
		else:
			return False

	def stack_size(self):
		return len(self.items)
		
"""
To find the smallest element in stack
We need to have a function which determines
the element which is being added is smallest or not.
If the element is first element we need to consider it as smallest and add it in the stack2
If we are appending new item we need to compare it with the value in stack2,
if it is small we need to append it to the the stack.
While pop operation we need to take care that the element in stack to is also popped.
"""
stack1 = Stack()
stack2 = Stack()


def push_item(item):
	
	if stack1.is_empty() is True:
		stack1.push(item)
		stack2.push(item)
	else:
		stack1.push(item)
		s2_item = stack2.peek()
		if s2_item > item:
			stack2.push(item)


def pop_item():
	s1_item = stack1.peek()
	s2_item = stack2.peek()
	if s1_item == s2_item:
		stack1.pop()
		stack2.pop()
	elif s1_item > s2_item:
		stack1.pop()

push_item(4)
push_item(5)
push_item(8)
push_item(3)
push_item(23)
push_item(15)
pop_item()
pop_item()
pop_item()