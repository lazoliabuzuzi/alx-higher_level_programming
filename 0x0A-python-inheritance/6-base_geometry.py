#!/usr/bin/python3
"""Defines a class BaseGeometry."""


class BaseGeometry:
    """A base class for geometry.

    Methods:
        area (self): raises an Exception with the message
        area() is not implemented.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Shows the area method is not implemented.
        """
        raise Exception("area() is not implemented")
