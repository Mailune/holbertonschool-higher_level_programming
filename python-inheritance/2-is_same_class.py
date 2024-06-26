#!/usr/bin/python3

"""Module for is_same_class function"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
    True if object is exactly an instance of specified class; otherwise False.
    """
    return type(obj) is a_class
