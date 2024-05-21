#!/usr/bin/python3
"""
Print a square
"""


def print_square(size):
    """
    Print a square of '#' characters with the given size.

    Parameters:
        size (int): The size of the square

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Example:
        >>> print_square(3)
        ###
        ###
        ###
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for t in range(size):
            print("#", end="")
        print()
