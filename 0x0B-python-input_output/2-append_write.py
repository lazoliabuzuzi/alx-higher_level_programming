#!/usr/bin/python3
"""Define a function that appends text to a file."""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file.
        text (str): The string to be written to the file.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
