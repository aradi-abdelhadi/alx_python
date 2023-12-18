"""This module defines the Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """
    Represents a geometric rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): An optional identifier for the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner. Default is 0.
            y (int, optional): The y-coordinate of the top-left corner. Default is 0.
            id (int, optional): An optional identifier for the rectangle.
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        self._validate_width()
        self._validate_height()
        self._validate_x()
        self._validate_y()

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x-coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x-coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y-coordinate of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    
    def _validate_width(self):
        """Validate the width attribute."""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")

    def _validate_height(self):
        """Validate the height attribute."""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height <= 0:
            raise ValueError("height must be > 0")

    def _validate_x(self):
        """Validate the x attribute."""
        if not isinstance(self.__x, int):
            raise TypeError("x must be an integer")
        if self.__x < 0:
            raise ValueError("x must be >= 0")

    def _validate_y(self):
        """Validate the y attribute."""
        if not isinstance(self.__y, int):
            raise TypeError("y must be an integer")
        if self.__y < 0:
            raise ValueError("y must be >= 0")
    
    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle, calculated as width * height.
        """
        return self.__width * self.__height
    
    def display(self):
        """
        Display the rectangle using '#' characters.

        This method prints a visual representation of the rectangle
        using '#' characters. Each row of the rectangle is printed on
        a new line, and the number of '#' characters in each row is
        determined by the width of the rectangle.

        Example:
        If the rectangle has width = 5 and height = 3, calling display()
        will output:
        #####
        #####
        #####

        Note: This method assumes that the width and height values are
        non-negative integers.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)
    
    def __str__(self):
        """
        Overrides __str__

        Returns:
            formatted string of rectange attributes.
        """
        return("[Rectangle] ({}) {}/{} - {}/{}").format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args, **kwargs):
        """
        Update the attributes of the Rectangle object and return a formatted string representation.

        This method allows updating the attributes of a Rectangle object using positional arguments.
        The arguments are expected to be in the order: [id, width, height, x, y]. After updating
        the attributes, the method returns a formatted string representation of the Rectangle object.

        Parameters:
        *args: Variable number of positional arguments representing the attributes to update,
               in the order [id, width, height, x, y].

        Returns:
        str: A formatted string representing the updated Rectangle object.
        """
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.__width = args[1]
            if num_args >= 3:
                self.__height = args[2]
            if num_args >= 4:
                self.__x = args[3]
            if num_args >= 5:
                self.__y = args[4]
        else: 
            for key, value in kwargs.items():
                setattr(self, key, value)
