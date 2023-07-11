#!/usr/bin/python3
"""Define a function that reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Read and print the contents of a UTF-8 file to stdout."""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end='')
