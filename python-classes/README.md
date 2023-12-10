# Python - Classes and Objects

This repository contains Python code for a task related to creating a `Square` class with private attributes for size. The purpose of this task is to demonstrate the use of classes and encapsulation in Python.

## Task Description

Write a class `Square` that defines a square with the following specifications:

- Private instance attribute: `size`
- Instantiation with size (no type/value verification)
- No import of any module

## Why Size is a Private Attribute

The `size` attribute is made private to control access and ensure proper encapsulation. The size of a square is a crucial parameter, and by keeping it private, we can control its type and value. This approach allows us to enforce conditions and validations on the attribute, providing a more robust and controlled implementation.

## File Structure

- `0-square.py`: Contains the implementation of the `Square` class.

## Usage Example

```python
Square = __import__('0-square').Square

# Create a square with size 3
my_square = Square(3)

# Print type and dictionary representation
print(type(my_square))
print(my_square.__dict__)

# Attempt to access size directly (should raise AttributeError)
try:
    print(my_square.size)
except AttributeError as e:
    print(e)

# Attempt to access __size directly (should raise AttributeError)
try:
    print(my_square.__size)
except AttributeError as e:
    print(e)

