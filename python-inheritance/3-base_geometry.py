"""
3-base_geometry

This module defines an empty base class for other geometry-related classes.
"""

class OverrideMetaClass(type):
    def __new__(cls, name, bases, attrs):
        # Customize the class creation process here
        return super().__new__(cls, name, bases, attrs)

    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(OverrideMetaClass('BaseGeometry', (), {})):
    """
    This class serves as the base for other geometry-related classes.
    """
    pass
    def __dir__(cls):
        """
        Returns:
            list: List of attributes excluding __init_subclass__.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']
       
