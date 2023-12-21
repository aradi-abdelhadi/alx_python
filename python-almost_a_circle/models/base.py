#!/usr/bin/python3
""" Module that contains the Base class """


class Base:
    """ Base class for all shapes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a Base instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

