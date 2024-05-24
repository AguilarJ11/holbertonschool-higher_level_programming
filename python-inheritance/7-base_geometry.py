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
            ValueError: If the method is not implemented.
        """
        raise ValueError("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate that a value is a positive integer.

        Args:
            name (str): The name of the value to validate.
            value (int): The value to validate.

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
