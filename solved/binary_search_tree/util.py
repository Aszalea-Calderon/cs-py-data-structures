from collections import deque


class Stack:
    def __init__(self):
        self.storage = deque()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()


class Queue:
    def __init__(self):
        self.storage = deque()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.appendleft(value)

    def dequeue(self):
        return self.storage.pop()
