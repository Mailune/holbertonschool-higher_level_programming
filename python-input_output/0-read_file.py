#!/usr/bin/python3
"""
This module contain a function read_file
"""


def read_file(filename=""):
    """ a function that open a file"""
    with open(filename, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        print(contenu, end="")
