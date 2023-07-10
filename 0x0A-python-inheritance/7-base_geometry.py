#!/usr/bin/python3
"""Define a class BaseGeometry."""


class BaseGeometry:
    """A base class for geometry.

    Methods:
        area (self): Raises an Exception with the message:
        "area() is not implemented."
        integer_validator(self, name, value): Validates the
        given value as an intger.
    """

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Shows the area method is not implemented.
    """

    def integer_validator(self, name, value):
        """Validate the given value as an integer.

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
