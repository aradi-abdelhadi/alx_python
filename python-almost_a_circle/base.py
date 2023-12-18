#!/usr/bin/python3
"""
models/base.py

This module defines the Base class, which serves as the base class for other classes in the project.

Classes:
    Base: The base class with private class attribute __nb_objects and public instance attribute id.
"""

class Base:
    """
    Base class for the project.

    Attributes:
        __nb_objects (int): Private class attribute to keep track of objects.
        id (int): Public instance attribute representing the object's ID.

    Methods:
        __init__(self, id=None): Constructor for the Base class.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new instance of the Base class.

        Args:
            id (int, optional): ID for the instance. If not provided, it's auto-generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
