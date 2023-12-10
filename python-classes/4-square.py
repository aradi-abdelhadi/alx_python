"""
4-square.py - A module that defines the Square class with size validation, area calculation, and printing method.

This module contains the definition of the Square class, which represents a square with a private attribute 'size', a public method 'area', and 'my_print' method for printing the square.
"""

class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int, optional): The size of the square. Default is 0.
        """
        self.__size = size
        self.__validate_size()

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Parameters:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = value
        self.__validate_size()

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the character '#'.

        Prints:
            The square pattern with '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for

