#!/usr/bin/python3

""" Module for MyList class """


class MyList(list):
    """A subclass of list that includes a method to print the list sorted"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
