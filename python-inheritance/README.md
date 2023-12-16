# is_same_class Module

This module provides a function to check if an object is exactly an instance of a specified class.

## Function

### `is_same_class(obj, a_class)`

Check if an object is exactly an instance of a specified class.

#### Parameters

- `obj`: The object to be checked.
- `a_class`: The specified class for comparison.

#### Returns

- `True` if the object is exactly an instance of the specified class, `False` otherwise.

## Example

```python
a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))

