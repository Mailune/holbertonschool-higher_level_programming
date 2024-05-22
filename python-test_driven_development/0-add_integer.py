#!/usr/bin/python3
"""

Module composed by a function that make the add of two numbers

"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float. Defaults to 98.

    Returns:
        The sum of the two numbers as an integer.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast to integers if they are floats
    a = int(a)
    b = int(b)

    return a + b
