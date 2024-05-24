#!/usr/bin/python3
"""
This module contains the definition of the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class: a base class for geometries.
    """

    def area(self):
        """
        Abstract method to calculate the area.

        Raises:
            Exception: If the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate that a value is a positive integer.

        Args:
            name (str): The name of the value to validate.
            value (int): The value to validate.

        Returns:
            bool: True if the value is a positive integer, False otherwise.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return True


class Rectangle(BaseGeometry):
    """
    Rectangle class: represents a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        if BaseGeometry.integer_validator("width", width):
            self.__width = width
        if BaseGeometry.integer_validator("height", height):
            self.__height = height
