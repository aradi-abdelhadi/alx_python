#!/usr/bin/python3

"""
This module contains a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class for comparison.

    Returns:
    - True if the object is an instance of a class that inherits from the specified class,
      False otherwise.
    """
    return issubclass(type(obj), a_class)

# Test cases
if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))

    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))

    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))

