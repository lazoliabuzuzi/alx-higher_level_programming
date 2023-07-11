#!/usr/bin/python3
"""Define a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first_name of the student.
            last_name (str): The last_name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, Optional): A list of attribute names to retrieve.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary representing the attributes of the
            Student instance.
        """
        for key, value in json.items():
            setattr(self, key, value)
