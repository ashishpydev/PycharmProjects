import heapq


class PriorityQueue:
    def __init__(self):
        self.items = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.items, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.items)[-1]


q = PriorityQueue()
q.push('foo', 1)
q.push('bar', 5)
q.push('spam', 4)
q.push('grok', 1)
print(q.pop())
