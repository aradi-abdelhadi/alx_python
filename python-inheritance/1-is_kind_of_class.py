#!/usr/bin/python3

"""
This module contains a function to check if an object is an instance of, or if the object
is an instance of a class that inherited from, the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class for comparison.

    Returns:
    - True if the object is an instance of or inherits from the specified class, False otherwise.
    """
    return isinstance(obj, a_class)

# Test cases
if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))

    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))

    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))

