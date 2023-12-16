# is_same_class Module

This module provides functions to check relationships between objects and classes.

## Functions

### `is_same_class(obj, a_class)`

Check if an object is exactly an instance of a specified class.

#### Parameters

- `obj`: The object to be checked.
- `a_class`: The specified class for comparison.

#### Returns

- `True` if the object is exactly an instance of the specified class, `False` otherwise.

### `is_kind_of_class(obj, a_class)`

Check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

#### Parameters

- `obj`: The object to be checked.
- `a_class`: The specified class for comparison.

#### Returns

- `True` if the object is an instance of or inherits from the specified class, `False` otherwise.

## Example

```python
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))

if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))

