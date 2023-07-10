#!/usr/bin/python3
"""Defines a class that inherits from list."""


class MyList(list):
    """A class that inherits from the list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
