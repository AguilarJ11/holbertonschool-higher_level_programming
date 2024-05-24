#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
This module contains the definition of the Rectangle Subclass.
"""


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
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        Returns:
            str: A string representing the Rectangle object in the format
            '[Rectangle] width/height', where 'width' and 'height' are the
            width and height of the rectangle, respectively.
        """
        return f"[Rectangle] {self.width}/{self.height}"
