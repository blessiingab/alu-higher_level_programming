#!/usr/bin/python3
"""
This module defines a Square class with attributes for size and position.
It includes methods for computing the area and printing the square with proper formatting.
"""


class Square:
    """
    A class that defines a square with size and position attributes.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size and position.
        
        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The position of the square, default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.
        
        Args:
            value (tuple): A tuple of two non-negative integers representing position.
        
        Raises:
            TypeError: If position is not a tuple of two non-negative integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#', considering the position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        
        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square using '#' characters.
        """
        if self.__size == 0:
            return ""
        
        result = "\n" * self.__position[1]
        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"
        
        return result.rstrip()
