#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns the print() and str() representation of a Rectangle."""
        return (f"[Rectangle] {self.__width}/{self.__height}")
