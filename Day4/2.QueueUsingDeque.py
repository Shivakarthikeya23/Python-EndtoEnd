from collections import deque


class Queue:
    def __init__(self):
        self.q = deque()

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.q.popleft()
        return None

    def front(self):
        return self.q[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.q) == 0


# Usage
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue())  # 1
print(q.front())  # 2
