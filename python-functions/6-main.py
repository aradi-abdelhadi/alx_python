#!/usr/bin/env python3
validate_password = __import__('6-password').validate_password

# Test cases
print(validate_password("Password123"))   # Output: True
print(validate_password("abc123"))         # Output: False
print(validate_password("Password 123"))   # Output: False
print(validate_password("password123"))    # Output: False

