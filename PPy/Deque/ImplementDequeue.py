class Deque:
	def __init__(self):
		self.items = []
	
	def enqueue_rear(self, item):
		self.items.insert(0, item)
		
	def enqueue_front(self, item):
		self.items.append(item)
	
	def dequeue_rear(self):
		item = self.items.pop(0)
		return item
		
	def dequeue_front(self):
		item = self.items.pop()
		return item
	
	def is_empty(self):
		return len(self.items) == 0
	
	def size(self):
		return len(self.items)


def palindrome():
	deque = Deque()
	word = "radar"
	for ch in word:
		deque.enqueue_rear(ch)
	while deque.size() > 1:
		r = deque.dequeue_rear()
		f = deque.dequeue_front()
		if r == f:
			print("Checked for the Letter: {} and {}".format(r, f))
			print(True)
		else:
			print("Checked for the Letter: {} and {}".format(r, f))
			print(False)

palindrome()
