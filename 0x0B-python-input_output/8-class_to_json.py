#!/usr/bin/python3
"""Define a dictionary description."""


def class_to_json(obj):
    """Return a dictionary description with simple data structure."""
    return obj.__dict__
