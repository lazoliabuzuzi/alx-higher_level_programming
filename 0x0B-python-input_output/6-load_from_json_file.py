#!/usr/bin/python3
"""Define a JSON file object."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.

    Args:
        filename (str):  The name of the JSON file.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, "r") as file:
        return json.load(file)
