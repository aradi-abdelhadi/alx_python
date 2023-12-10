class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
            size (int): The size of the square.
        """
        self.__size = size

# Test the Square class
if __name__ == "__main__":
    my_square = Square(3)

    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)  # This should raise an AttributeError
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)  # This should raise an AttributeError
    except AttributeError as e:
        print(e)

