#!/usr/bin/python3
"""Defines a JSON string object."""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to be parse.

    Returns:
        obj: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
