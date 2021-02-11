"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_min`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from util import Stack, Queue  # these may be used in traversals


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.left = self.right = None


    # Insert the given value into the tree
    def insert(self, new_value):
        if new_value < self.value:# if newvalue is less than the value of the new node
            # go left
            if self.left:
                #we have a left child
                # let the left child deal with the new value
                self.left.insert(new_value) # recursion, This then takes
            else:
                #since we don't have a left child,
                # we'll make this value a Node, and make it our new left child
                self.left = BSTNode(new_value)

        else:
            # new_value is larger than or equal to self.value
            if self.right:# if our right child exists
                # let the right child deal with new_value
                self.right.insert(new_value)
            else: # our right child does NOT exist
                # so make a node with new_value and make that our right child
                self.right = BSTNode(new_value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        # Loop thourgh each of the current_nodes on the right, this goes through each until we hit None
        while current_node.right is not None:
            current_node = current_node.right

        # then we return the value of the current node with the value
        return current_node.value


    def get_min(self):
        current_node = self
        # Loop thourgh each of the current_nodes on the right, this goes through each until we hit None
        while current_node.left is not None:
            current_node = current_node.left

        # then we return the value of the current node with the value
        return current_node.value
        # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


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
