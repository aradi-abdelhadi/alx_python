#!/usr/bin/python3

"""
6-rectangle
It contains the definition of the Rectangle class.
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
    - __width (int): Private width of the rectangle.
    - __height (int): Private height of the rectangle.
    """

    def __init__(self, width, height):
        """Instantiates a Rectangle object with a given width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculates and returns the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle with '#' characters."""
        for i in range(self.__height):
            print("#" * self.__width)

    def integer_validator(self, name, value):
        """Validates that the value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

# Test cases
if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.__width, r.__height))
    except AttributeError as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except (TypeError, ValueError) as e:
        print("[{}] {}".format(e.__class__.__name__, e))

