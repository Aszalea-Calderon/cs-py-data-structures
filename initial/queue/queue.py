"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from ../singly_linked_list.singly_linked_list import LinkedList
from collections import deque

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):#this is how you do .length
        self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        self.size  -= 1
        return self.storage.remove_head()

class DQueue:
    def __init__(self):
        self.storage = deque()

    def __len__(self):#this is how you do .length
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.popleft()

