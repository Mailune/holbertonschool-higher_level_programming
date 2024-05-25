#!/usr/bin/python3
""" Module for is_kind_of_class method"""


class BaseGeometry:
    """
    Base class representing geometry.

    This class provides a base for geometric shapes.
    """

    def area(self):
        """
        Calculate the area of the geometric shape.

        Raises:
            Exception: Always raises an exception with the message
                'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
