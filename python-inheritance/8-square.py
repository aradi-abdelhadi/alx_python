#!/usr/bin/python3

"""
8-square
It contains the definition of the Square class.
"""

Rectangle = __import__('7-rectangle').Rectangle

class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
    - __size (int): Private size of the square.
    """

    def __init__(self, size):
        """Instantiates a Square object with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

# Test case
if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())

