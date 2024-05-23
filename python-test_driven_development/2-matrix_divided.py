#!/usr/bin/python3
"""
This module defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): Matrix to be divided.
        div (int or float): Number to divide the matrix by.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    Returns:
        list of lists: New matrix with all elements divided by div.
    """
    error_msg = ("matrix must be a matrix (list of lists) of "
                 "integers/floats")

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float)) for row in matrix
                    for num in row)):
        raise TypeError(error_msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
