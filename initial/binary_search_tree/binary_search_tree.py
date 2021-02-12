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
# from util import Stack, Queue  # these may be used in traversals
from collections import deque # Said deck double que.

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f"BSTNode({self.value})"
        # self.left = self.right = None

    def __contains__(self, item):
        return self.contains(item)  # This build it into the python language. It is obj oriented programing. huzzah!


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
        if self.value == target:  # This is the current node, Its in front
            return True # yay! We did it

        if self.value > target: # Go left
            if self.left is None:  # check if there is none
                return False # It doesn't exist
            else:
               return self.left.contains(target)
        else: # go right because it is greater than our value or the same
            if self.right is None: # Checking for nothing. Does it exist?
                return False
            else:  # This is checking the next right node.
               return self.right.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self
        # Loop through each of the current_nodes on the right, this goes through each until we hit None
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
            # Hey I have a node, I want to print the value in the tree from smallest to biggest!
            # We are using the call stack it will stack in the order we set up. Below!
        if self.left: # if self.left exists. If more lefts
            self.left.in_order_print()  # call back dat function
        print(self.value)

        if self.right:
            self.right.in_order_print()



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # add on one side and remove from the other. Be consistent.
    def bft_print(self):
        q = deque()  # Using this instead of self implemented queue because its better
        q.append(self)  # This adds self. (current_node) to the tail of the queue
        print(q)  #
        while len(q) !=0:
            print(q)
            # this can be implmented instead of recurrsion
            current_node = q.popleft() # This removes from the beginning
            print(current_node.value)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)


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
# bst = BSTNode(1)
#
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
#
# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_print()
# print("post order")
# bst.post_order_dft()

if __name__ == '__main__':
    bst = BSTNode(8)
    bst.insert(2)
    bst.insert(10)
    bst.insert(40)
    bst.insert(50)
    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(8)
    max_val = bst.get_max()
    min_val = bst.get_min()
    # print(max_val)  # 40
    # print(min_val)  # 2
    # # bst.contains(2)
    # print(bst.contains(2))
    # print(2 in bst)
    #bst.in_order_print()
    bst.bft_print()