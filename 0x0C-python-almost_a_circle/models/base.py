#!/usr/bin/python3
"""Define a class Base."""


class Base:
    """Private class attribute to keep track of
    objects created."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
