#!/usr/bin/python3

"""
3-base_geometry
It contains an empty class call BaseGeometry

"""
class OverrideMetaClass(type):
    """
        This is a meta class created to inform the behaviour of the BaseGeometry class.
        It's the base class for the BaseGeometry class
    """
    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super.__dir__() if attribute != '__init_subclass__']
class BaseGeometry(OverrideMetaClass('BaseGeometry', (), {})):
    """This is an empty class.
    The Pass keyword is used to print an empty line
    """
    pass

    def __dir__(cls):
        """This is used to check the list of attributes in the dir magic class.
        It ensures that __init_subclass__ is not printed"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """It's used to raise an exception that the area method is not implemented
        """
        raise Exception ('area() is not implemented')
