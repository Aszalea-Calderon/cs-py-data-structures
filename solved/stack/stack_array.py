class Stack:
    """
    A stack is a data structure whose primary purpose is to store and return
     elements in Last-In, First-Out  (LIFO) order.
    """

    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage.append(value)  # add to tail

    def pop(self):
        if not self.storage:
            return None  # nothing to delete, nothing to return

        return self.storage.pop()  # remove from tail
