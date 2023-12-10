class Square:
    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

# Test the Square class
if __name__ == "__main__":
    mysquare = Square(3)

    print(type(mysquare))
    print(mysquare.__dict__)

    try:
        print(mysquare.size)  # This should raise an AttributeError
    except AttributeError as e:
        print(e)

    try:
        print(mysquare.__size)  # This should raise an AttributeError
    except AttributeError as e:
        print(e)

    # Accessing and modifying size using getter and setter
    print(mysquare.get_size())

    mysquare.set_size(5)
    print(mysquare.get_size())

