class Queue:
    def __init__(self):
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if not self.storage:
            return None  # nothing to remove, nothing to return

        return self.storage.pop()
