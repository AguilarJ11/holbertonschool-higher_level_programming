#!/usr/bin/python3

"""
This module contains the definition of the Square Subclass.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class: represents a square,
        subclass of Rectangle
    Attributes:
        __size (int): The size of the square,
    which is equal to both width and height.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        if self.integer_validator("size", size):
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
