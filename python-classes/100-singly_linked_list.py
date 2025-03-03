#!/usr/bin/python3

class Node:
    """Defines a node of a singly linked list."""
    
    def __init__(self, data, next_node=None):
        """Initialize a node with data and optional next_node."""
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Getter for data attribute."""
        return self.__data
    
    @data.setter
    def data(self, value):
        """Setter for data attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Getter for next_node attribute."""
        return self.__next_node
    
    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute with validation."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""
    
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None
    
    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position (increasing order)."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
    
    def __str__(self):
        """Returns a string representation of the linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
