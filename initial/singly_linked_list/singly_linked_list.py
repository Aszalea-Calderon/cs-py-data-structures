class Node:
    """
    A class representation of a DoublyLinkedList Node.

    Each Node will store
    (1) a value (could be of any type) and
    (2) a reference to the next_node Node in list.

    doc string- This can go under a class or function. This is great for doc's and comments. 
    """

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value}"


class LinkedList:
    """
    A class representation of a Singly-Linked-List.

    Stores a reference to
    (1) the head (first node in list) and
    (2) the tail (last node in list).

    Each item in list will be an instance of class Node (defined above) and
    each node instance will store a value and a reference to the next_node Node in list.

    This just keeps track of the first and last node. This will hold the A node and Z node and holds its own
    """

    def __init__(self):
        """
        Constructs a new instance of a DoublyLinkedList
        """
        # NOTE: Nothing to do in here right now
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        """
        Adds a Node with the given value to the beginning of the list

        :param value: the value to store at the beginning of the list
        :return: None
        """
        new_node = Node(value)
         #Above makes a new node instance with a given value, This comes from the class Node

        if self.head is None:
            #if there are no items in the list
            self.head = new_node
            self.tail = new_node
            return #we return if there were no items in the list



        new_node.next = self.head 
        #Next assign new node.next the current head 
        self.head = new_node
         #Assign new node as the new head, this reassigns the current head to be the new value.

    def add_to_tail(self, value):
        """
        Adds a Node with the given value to the end of the list

        :param value: the value to store at the end of the list
        :return: None
        """
        new_node = Node(value)

        if self.head is None:#if there are no items in the list
            self.head= self.tail = new_node
            #above and below are the same thing! =)
            # self.head = new_node
            # self.tail = new_node
            return

        self.tail.next = new_node #this puts new node after self.tail. It would be in the E spot. 
        self.tail = new_node #this points to the new tail. 

    def remove_head(self):
        """
        Remove the item at the beginning of the list.

        :return: The value of the item being removed
        """
        
        #If list is empty, then there is nothing to delete. 
        if self.head is None:
            return
        
        old_head_value = self.head.value #We make a copy before we delete it. We will not be able to access it after we delete it

        if self.head.next is None:#This checks if the list has only one item
            self.tail = None



        print(old_head_value)
        self.head = self.head.next #this shifts the head pointer from current head "a" to b. 
        return old_head_value 




    def remove_tail(self):
        """
        Remove the item at the end of the list.

        :return: The value of the item being removed
        """
        if self.head is None:#This checks if nothing is in the list.
            return
        old_tail_value = self.tail.value

        
        if self.head.next is None:
            self.head = self.tail = None
            return old_tail_value

        current_node = self.head #this assigns it to the first item, Then it hits the while loop

        while current_node.next is not self.tail: #This then goes through each item until it is the second to last one,
            current_node = current_node.next#keeps checking until the end

        #This then assigns the next to Node to nothing
        current_node.next = None
        self.tail = current_node
        return old_tail_value