#!/usr/bin/python3
"""
Addition
"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer of float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)

    if isinstance(b, float):
        b = int(b)

    return int(a + b)
