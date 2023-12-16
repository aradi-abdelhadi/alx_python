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
    return type(obj) == a_class

# Test cases
if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))

    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))

    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))

# New line added below
