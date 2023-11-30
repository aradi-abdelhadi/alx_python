#!/usr/bin/env python3
convert_to_celsius = __import__('2-temperature').convert_to_celsius

# Test cases
print(convert_to_celsius(100))      # Output: 37.77777777777778
print(convert_to_celsius(-40))      # Output: -40
print(convert_to_celsius(-459.67))  # Output: -273.15
print(convert_to_celsius(32))       # Output: 0.0

