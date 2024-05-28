#!/usr/bin/python3
"""Module defining the Student class"""


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if attrs is not None and isinstance(attrs, list):
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr)
            }
        else:
            return self.__dict__
