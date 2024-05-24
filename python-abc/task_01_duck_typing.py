#!/usr/bin/env python3

"""
Abstract base class representing a shape
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for different shapes.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        This method should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        This method should be implemented by subclasses.
        """
        pass


"""
A subclass representing a circle
"""


class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance with a given radius.

        Parameters:
            radius (float): The radius of the circle.
        """
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError("radius must be an integer or float")
        elif radius < 0:
            raise ValueError("radius must be greater or equal than 0")
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return math.pi * (self.radius * 2)


"""
A subclass representing a rectangle
"""


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with a given width and height.

        Parameters:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if not (isinstance(width, int) or isinstance(width, float)) \
                or not (isinstance(height, int) or isinstance(height, float)):
            raise TypeError("width and height must be integers or floats")
        elif width < 0 or height < 0:
            raise ValueError("width and height must be greater or equal than 0")
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


"""
Function to print the area and perimeter of a given shape object.
"""


def shape_info(obj):
    """
    Print the area and perimeter of a given shape object.

    Parameters:
        obj (Shape): An instance of a subclass of Shape.
    """
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
