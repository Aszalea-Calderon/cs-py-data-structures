"""
This is a quick and dirty implementation of a queue.
If you're coding on the GCA, my personal recommendation for
implementing a queue would look like this.
"""
from collections import deque


class Queue:
    def __init__(self):
        self.storage = deque()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.appendleft(value)  # add to front

    def dequeue(self):
        return self.storage.pop()  # remove from back
