#!/usr/bin/python3
"""
This module contains function to save an object to a JSON file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
