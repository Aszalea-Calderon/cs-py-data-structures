from typing import Optional


class Node:
    """
    Each Node holds a reference to its previous node
    as well as its next_node node in the List.
    """

    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
       
    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    """
    Our doubly-linked list class. It holds references to
    the list's head and tail nodes.
    """

    def __init__(self, node_list: Optional[list] = None):
        self.head = self.tail = None  # initialize head and tail to None
        self.size = 0  # number of items stored in DLL
        # if given node_list exists
        if node_list is not None:
            # then add each value in list to tail
            for value in node_list:
                self.add_to_tail(value)

    def __repr__(self):
        """Returns a string representation of this DoublyLinkedList"""

        str_repr = "DLL=["
        if self.size == 0:
            return f"{str_repr}]"
        current_node = self.head
        while current_node is not None:
            str_repr += f"{current_node}{']' if current_node is self.tail else ' -> '}"
            current_node = current_node.next
        return str_repr

    def __len__(self):
        return self.size

    def add_to_head(self, value):
        """
        Wraps the given value in a Node and inserts it
        as the new head of the list. Don't forget to handle
        the old head node's previous pointer accordingly.
        """
        new_node = Node(value)
        if self.size == 0: 
            self.head = self.tail = new_node # this is assigning it to both because there is nothing!!
        else:
            new_node.next = self.head  # New node will before the current head
            self.head.prev = new_node  # The current head will be after the new node 
            self.head = new_node # This assigns the new linked list to be the new node head
        self.size +=1 # this adds to the size

        # yay! We did it. 

    def remove_head(self):
        """
        Removes the List's current head node, making the
        current head's next_node node the new head of the List.
        Returns the value of the removed Node.
        """

        if self.size == 0:
            return

        removed_value = self.head.value  # This grabs the value of current head so when it is deleted we can actually return it.

        if self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next  # Shifts head to the right. NICE! =D
            self.head.prev = None  # Says there is nothing before the new head. 

        self.size -= 1  # Changes the size of the list 

        return removed_value


    def add_to_tail(self, value):
        """
        Wraps the given value in a Node and inserts it
        as the new tail of the list. Don't forget to handle
        the old tail node's next_node pointer accordingly.
        """
        new_node = Node(value)

        if self.size == 0: 
            self.head = self.tail = new_node  # this is assigning it to both because there is nothing!!

        else:
            self.tail.next = new_node  # place new_node after tail 
            new_node.prev = new_node  # place current tail before new_node
            self.tail = new_node  # replace self.tail
            
        self.size +=1  # increase size of list

    def remove_tail(self):
        """
        Removes the List's current tail node, making the
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        """
        if self.size == 0:
            return

        value_to_remove = self.tail.value  # This grabs the value of current head so when it is deleted we can actually return it.

        if self.size == 1:
            self.head = self.tail = None

        else:
            self.tail = self.tail.prev  # This assigns it to the prior tail
            self.tail.next = None  # Nothing comes after this new tail. NOTHING. 

        self.size -= 1
        return value_to_remove


    def move_to_front(self, current_node):
        """
        Removes the input current_node from its current spot in the
        List and inserts it as the new head current_node of the List.
        """
        if self.size == 0:
            return
        # Oh my, people suck sometimes*, lets check dat current_node
        if not current_node or (not current_node.next and not current_node.prev):
            # This is saying if current_node is not existant aka none (not current_node) 
            # or current_node is not attached to anything. aka falsey that it is part of the list. It checks if it equals to 1. You can't move the item of position 1 to item position 1
            return
        if self.head is current_node:
            return
            # if the current_node is already at the head, why you moving it bro?
        if self.tail is current_node:
            self.tail = current_node.prev
        else:
            current_node.next.prev = current_node.prev
        current_node.prev.next = current_node.next
        
        self.head.prev = current_node
        current_node.next = self.head
        current_node.prev = None
        self.head = current_node

    def move_to_end(self, node):
        """
        Removes the input node from its current spot in the
        List and inserts it as the new tail node of the List.
        """
        pass

    def delete(self, node):
        """
        Deletes the input node from the List, preserving the
        order of the other elements of the List.
        """
        pass

    def get_max(self):
        """
        Finds and returns the maximum value of all the nodes
        in the List.
        """
        pass
