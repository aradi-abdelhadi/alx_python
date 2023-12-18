#!/usr/bin/python3

class BaseGeometry:
    """
    This module defines a class called BaseGeometry.

    The BaseGeometry class serves as a foundation for geometry-related classes.
    It includes a public instance method area() that raises an Exception with the message "area() is not implemented".

    Attributes:
    - No attributes are defined in this class.

    Methods:
    - area(self): Raises an Exception with the message "area() is not implemented".
    """
    def area(self):
        """
        Raises:
        - Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

