"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.

Binary Search trees are ORDERED —
traditionally:
 - highest key will be rightmost node,
 - lowest key will be leftmost node,
 - in theory, middle node will be ROOT (if we code correctly)

"""
from util import Stack, Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given key into the tree
    def insert(self, value):  # either create or insert
        # if value == self.value:
        #     return

        if value < self.value:
            if self.left is not None:
                self.left.insert(value)  # recurse
            else:
                self.left = BSTNode(value)
        else:  # go to right
            if self.right is not None:
                self.right.insert(value)  # recurse
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the key
    # False if it does not
    def contains(self, target):

        if self.value == target:  # current node is target
            return True

        elif self.value < target:  # go right b/c current node is smaller than target
            if self.right is None:  # if there is no node to the right
                return False  # target does not exist in tree

            else:  # else, there is a right
                return self.right.contains(target)  # so recurse with right node

        else:  # go left b/c current node is greater than target
            if self.left is None:  # if no node to the left
                return False  # target does not exist in tree

            else:  # else, there is a left
                return self.left.contains(target)  # recurse with left node

    # Return the maximum key found in the tree
    def get_max(self):
        # max should be the rightmost node
        current = self

        while current.right is not None:  # while current.right exists
            current = current.right  # move right down the tree

        # once we reach here, we're at rightmost node (highest key)
        return current.value

    # Call the function `fn` on the key of each node
    def for_each(self, fn):
        fn(self.value)

        # create one large callstack then call all together
        # continue until end — these do not run simultaneously
        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:  # if left, call for left
            self.left.in_order_print()

        print(self.value)  # if no left, print current

        if self.right:  # if right, call for right
            self.right.in_order_print()

    # Print the key of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # we use a queue for Breadth-first FIFO (think grocery-store line)
        queue = Queue()
        queue.enqueue(self)
        while len(queue) != 0:  # while there is anything in the queue
            current = queue.dequeue()
            print(current.value)
            if current.left:
                queue.enqueue(current.left)

            if current.right:
                queue.enqueue(current.right)

    # Print the key of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # use a test_stack for depth-first LIFO (think pancakes)
        stack = Stack()
        stack.push(self)  # add current to test_stack
        while len(stack) != 0:  # while there is something in our test_stack
            current = stack.pop()
            print(current.value)
            if current.left:
                stack.push(current.left)

            if current.right:
                stack.push(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self:
            print(self.value)  # print current first
            if self.left:
                self.left.pre_order_dft()

            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self:
            if self.left:
                self.left.post_order_dft()

            if self.right:
                self.right.post_order_dft()

            print(self.value)  # print current last


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
