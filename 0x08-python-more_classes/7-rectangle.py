#!/usr/bin/python3
"""Define a class Rectangle."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height if the rectangle.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height of the rectangle."""
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return self.__width * self__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Defines the string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += str(self.print_symbol) * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """Defines the string representation of the rectangle object."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when an instance of rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
