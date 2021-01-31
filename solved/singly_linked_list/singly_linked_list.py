class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        pass

    def add_to_head(self, value):
        pass

    def remove_head(self):
        pass

    def remove_tail(self):
        pass
