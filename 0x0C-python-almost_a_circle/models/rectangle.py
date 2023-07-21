#!/usr/bin/python3
"""Define a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The identity of the rectangle.

        Raises:
            TypeError: if width or height are not integers.
            ValueError: if width or height is <= 0.
            TypeError: if x or y are not integers.
            ValueError: if x or y is <= 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height if the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle instance."""
        return self.width * self.height

    def display(self):
        """Display the rectangle using '#'."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Override the str method to change the string representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args):
        """Update the attributes of the rectangle."""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: Positional arguments, which will be ignored if **kwargs
            is provided.
            **kwargs: Keyword arguments, where each key represents an
            attribute name,and the corresponding value is the new value for
            that attribute.

        Raises:
            TypeError: if any of the attribute values aren't integers.
            ValueError: if any of the attribute values are invalid (e.g.
            <= 0 for width/height, < 0 for x/y.)
        """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
