#!/usr/bin/env python3

def is_prime(number):
    """
    Checks if a given number is a prime number.

    :param number: The input number.
    :return: True if the number is prime, False otherwise.
    """
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

