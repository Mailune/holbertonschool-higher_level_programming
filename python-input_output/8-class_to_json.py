#!/usr/bin/python3
"""Module for converting class instances to JSON-compatible dictionaries"""


def class_to_json(obj):
    """
    Convert an instance of a class to a JSON-compatible dictionary.
    """
    json_dict = {}

    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            json_dict[attr_name] = attr_value

    return json_dict
