"""
This is a quick and dirty implementation of a stack.
If you're coding on the GCA, my personal recommendation for
implementing a stack would look like this.
"""
from collections import deque
class Stack:
    def __init__(self):
        self.storage = deque()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)  # add to tail

    def pop(self):
        if len(self.storage) == 0:
            return None  # nothing to remove, nothing to return

        return self.storage.pop()  # remove from tail