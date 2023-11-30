#!/usr/bin/env python3
pow = __import__('1-power').pow

# Test cases
result = pow(2, 2)
print("Correct output - case: pow(2, 2):", result)

result = pow(98, 2)
print("Correct output - case: pow(98, 2):", result)

result = pow(98, 0)
print("Correct output - case: pow(98, 0):", result)

result = pow(100, -2)
print("Correct output - case: pow(100, -2):", result)

result = pow(-4, 5)
print("Correct output - case: pow(-4, 5):", result)

