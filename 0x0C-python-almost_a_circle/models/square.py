#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square.

        Args:
            size (int): The size fo the square, width and height.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The identity of the square.

        Raises:
            TypeError: if size, x, or y are not integers.
            ValueError: if size, x or y is <= 0.
        """
        super().__init__(size, size, x, y, id)

        def __str__(self):
            """Override the str method to change the string representation."""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                     self.width)
