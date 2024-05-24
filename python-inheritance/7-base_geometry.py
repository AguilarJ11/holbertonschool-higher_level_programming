#!/usr/bin/python3
"""
A BaseGeometry class
"""


class BaseGeometry:
    """
    A empty class named BaseGeomery
    """
    pass

def area(self):
        raise ValueError("area() is not implemented")

def integer_validator(self, name, value):
    if not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    elif value <= 0:
        raise ValueError(f"{name} must be greater than 0")
    else: 
        return True
