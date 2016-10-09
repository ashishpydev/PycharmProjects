class Stack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, item):
        self.stack.append(item)
        if item > self.peek(self.max_stack):
            self.max_stack.append(item)
        print self.max_stack

    def pop(self):
        item = self.stack.pop()
        if item == self.peek(self.max_stack):
            self.max_stack.pop()
        print self.max_stack
        return item

    def get_max(self):
        max_item = self.peek(self.max_stack)
        return max_item

    def is_empty(self, stack):
        if len(stack) == 0:
            return True
        else:
            return False

    def peek(self, stack):
        if self.is_empty(stack) is False:
            temp = stack.pop()
            stack.append(temp)
            return temp
        else:
            return 0

s = Stack()
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.pop()
