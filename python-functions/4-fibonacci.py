#!/usr/bin/env python3

def fibonacci_sequence(n):
    """
    Generates the first n Fibonacci numbers.

    :param n: The number of Fibonacci numbers to generate.
    :return: A list of the first n Fibonacci numbers.
    """
    if n <= 0:
        return []

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]

