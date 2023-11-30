#!/usr/bin/env python3
fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence

# Test cases
print(fibonacci_sequence(6))    # Output: [0, 1, 1, 2, 3, 5]
print(fibonacci_sequence(1))    # Output: [0]
print(fibonacci_sequence(0))    # Output: []
print(fibonacci_sequence(20))   # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]

