#!/usr/bin/python3
"""
This module contains function convert a JSON string to a Python object
"""


import json


def from_json_string(my_str):
    """
    Return a Python data structure represented by a JSON string.
    """
    return json.loads(my_str)
