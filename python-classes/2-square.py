#!/usr/bin/python3

"""Square class definition"""


class Square:
    """Creates a square with a given size"""

    def __init__(self, size=0):
        """Initializes the size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
