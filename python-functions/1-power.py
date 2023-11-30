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
print("Correct output - case: pow(2, 2):", pow(2, 2))         # Output: 4
print("Correct output - case: pow(-2, 2):", pow(-2, 2))       # Output: 4
print("Correct output - case: pow(10, -2):", pow(10, -2))     # Output: 0.01
print("Correct output - case: pow(-98, -10):", pow(-98, -10))  # Output: 9.54231568545573e-26


