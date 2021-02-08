class Node:
    """
    A class representation of a DoublyLinkedList Node.

    Each Node will store
    (1) a value (could be of any type) and
    (2) a reference to the next_node Node in list.
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
        # TODO: IMPLEMENT THIS METHOD
        # Please note that the value coming in is NOT an instance of the Node class
        ###############################
        # wrap the given value in a Node and insert it as the new head of the list
        ###############################
        pass

    def add_to_tail(self, value):
        """
        Adds a Node with the given value to the end of the list

        :param value: the value to store at the end of the list
        :return: None
        """
        # TODO: IMPLEMENT THIS METHOD
        pass

    def remove_head(self):
        """
        Remove the item at the beginning of the list.

        :return: The value of the item being removed
        """
        # TODO: IMPLEMENT THIS METHOD
        pass

    def remove_tail(self):
        """
        Remove the item at the end of the list.

        :return: The value of the item being removed
        """
        # TODO: IMPLEMENT THIS METHOD
        pass
