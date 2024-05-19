#!/usr/bin/python3
"""
Square:
    Square
"""


class Square:
    """
    A class named Square.
    """
    def __init__(self, size=0):
        """
        Initialize the square with a size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
