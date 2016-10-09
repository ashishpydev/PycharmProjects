class Queue:
	def __init__(self):
		self.items = []
	
	def enqueue(self,item):
		self.items.insert(0, item)
		
	def dequeue(self):
		self.items.pop(0)
	
	def is_empty(self):
		return len(self.items) == 0
	
	def size(self):
		return len(self.items)
