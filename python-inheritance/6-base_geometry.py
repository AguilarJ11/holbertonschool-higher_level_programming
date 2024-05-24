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
        """
        Abstract method to calculate the area.
        
        Raises:
            ValueError: If the method is not implemented.
        """
        raise ValueError("area() is not implemented")
