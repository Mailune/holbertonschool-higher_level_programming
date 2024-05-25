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

    def integer_validator(self, name, value):
        """
        Validate the value for being an integer and being greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
