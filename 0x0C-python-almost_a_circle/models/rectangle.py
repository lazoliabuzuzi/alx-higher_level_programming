#!/usr/bin/python3
from models.base import Base
"""Define a class Rectangle."""


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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Width must be a positive integer.")
        self.__width = value

    @property
    def height(self):
        """Gets the height if the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Height must be a positive integer.")
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise ValueError("x must be an integer.")

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise ValueError("y must be an integer.")
