#!/usr/bin/python3
"""Define a function that writes to a file."""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the
    number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be wrriten to the file.

    Returns:
        The number of characters to be written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
