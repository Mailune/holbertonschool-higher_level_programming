#!/usr/bin/python3

"""
This module defines a class Rectangle.
"""


class Rectangle:
    """Class for creating Rectangle objects."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance."""
        self.set_width(width)
        self.set_height(height)

    def get_width(self):
        """Get the width of the rectangle."""
        return self.__width

    def set_width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def get_height(self):
        """Get the height of the rectangle."""
        return self.__height

    def set_height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Compute the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += "#" * self.__width
            if i != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """Return a string representation of the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
