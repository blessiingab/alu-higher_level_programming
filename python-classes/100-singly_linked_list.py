#!/usr/bin/python3
"""
Module for implementing a singly linked list.

This module contains two classes:
- Node: Defines a node in the singly linked list.
- SinglyLinkedList: Implements a singly linked list with sorted insertion.
"""


class Node:
    """Defines a node of a singly linked list.
    
    Attributes:
        data (int): The data stored in the node.
        next_node (Node or None): Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialize a node with data and optional next_node.
        
        Args:
            data (int): The data value of the node.
            next_node (Node, optional): The next node in the linked list.
                Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data attribute."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data attribute with validation.
        
        Args:
            value (int): The data value to set.
        
        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node attribute."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node attribute with validation.
        
        Args:
            value (Node or None): The next node reference.
        
        Raises:
            TypeError: If value is not None or a Node instance.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list.
    
    Attributes:
        __head (Node or None): The head (first node) of the linked list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position (increasing order).
        
        Args:
            value (int): The value to insert into the list.
        """
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
        """Returns a string representation of the linked list.
        
        Returns:
            str: A string with each node value on a new line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
