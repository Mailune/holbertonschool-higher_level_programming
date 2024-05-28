#!/usr/bin/python3
"""
This module contains a function `write_file` to write text to a file.
"""


def write_file(filename="", text=""):
    """
    Write string to UTF-8 text file and return number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as fichier:
        nb_characters = fichier.write(text)
    return nb_characters
