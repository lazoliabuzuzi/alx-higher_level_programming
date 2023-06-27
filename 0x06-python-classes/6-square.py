#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size (int): Size of the new square. Default is 0.
            position (tuple): Position of the square. Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the sqaure."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @size.setter
    def position(self, value):
        """Set the position of the square."""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
                    raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
