#!/usr/bin/env python3
def add(a, b):
    """
    Adds two integers and returns the result.

    :param a: The first integer.
    :param b: The second integer.
    :return: The sum of a and b.
    """
    return a + b

# Test cases
print("Correct output - case: add(1, 2):", add(1, 2))        # Output: 3
print("Correct output - case: add(100, -2):", add(100, -2))  # Output: 98
print("Correct output - case: add(-100, -2):", add(-100, -2))  # Output: -102
print("Correct output - case: add(0, 0):", add(0, 0))          # Output: 0

