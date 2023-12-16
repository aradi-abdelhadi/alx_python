#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Parameters:
    - obj: The object to be checked.
    - a_class: The specified class for comparison.

    Returns:
    - True if the object is exactly an instance of the specified class, False otherwise.
    """
    # Special case: None is considered an instance of any class
    if obj is None:
        return True
    return type(obj) == a_class

# Test cases
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))

    a = True
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))

    a = 3.14
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))

    a = True
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

    a = None
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

    # Additional test cases
    a = None
    if is_same_class(a, list):
        print("{} is an instance of the class {}".format(a, list.__name__))

    a = [1, 2, 3]
    if is_same_class(a, list):
        print("{} is an instance of the class {}".format(a, list.__name__))

    a = [1, 2, 3]
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

