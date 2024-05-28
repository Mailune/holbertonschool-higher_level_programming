#!/usr/bin/python3
"""
This module contains a function `append_write` to append text to a file.
"""


def append_write(filename="", text=""):
    """
    Append string to UTF-8 text file and return the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as fichier:
        nb_characters = fichier.write(text)
    return nb_characters
