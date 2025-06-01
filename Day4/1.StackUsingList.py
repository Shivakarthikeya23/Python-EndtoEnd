class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

s= Stack()

s.push(20)
s.push(30)
s.push(10)
print(s.peek())
print(s.pop())
print(s.pop())