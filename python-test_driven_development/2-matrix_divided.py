#!/usr/bin/python3
"""
This module divides all elements of a matrix by a divisor
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a list of lists
        containing integers or floats,
        or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
        TypeError: If each row of the matrix does not have the same size.

    Returns:
        list of lists: A new matrix with each element divided by the divisor,
                       rounded to 2 decimal places.
    """
    row_length = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        if len(row) != row_length and row_length != 0:
            raise TypeError("Each row of the matrix must have the same size")
        row_length = len(row)
        for i in row:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    return [[round(x / div, 2) for x in row] for row in matrix]
