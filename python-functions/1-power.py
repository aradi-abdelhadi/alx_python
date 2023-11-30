#!/usr/bin/env python3
def pow(a, b):
    """
    Computes a to the power of b and returns the value.

    :param a: The base.
    :param b: The exponent.
    :return: The result of a to the power of b.
    """
    return a ** b

# Test cases
print(pow(2, 2))     # Output: 4
print(pow(98, 2))    # Output: 9604
print(pow(98, 0))    # Output: 1
print(pow(100, -2))  # Output: 0.0001
print(pow(-4, 5))     # Output: -1024

