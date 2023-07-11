#!/usr/bin/python3
"""Define a dictionary description."""
import sys


def class_to_json(obj):
    """Return a dictionary description with simple data structure.

    Args:
        object: An instance of a class.

    Returns:
        dict: The dictionary description with a simple data structure.
    """
    attributes = vars(obj)
    serialized = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[attr] = value

    return serialized
