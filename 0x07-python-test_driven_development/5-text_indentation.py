#!/usr/bin/python3
"""
Text indentation
"""


def text_indentation(text):
    """prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text (str): A string.

    Raises:
        TypeError: If not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = [".", "?", ":"]
    result = ""
    line = ""

    for char in text:
        line += char
        if char in punctuation_chars:
            result += line.strip() + "\n"
            line = ""

    result += line.strip()
    print(result)
