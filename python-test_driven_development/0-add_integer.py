#!/usr/bin/python3
"""
This module contains a function to add two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer or float to be added.
        b (int or float, optional): The second integer or float to be added.
            Defaults to 98.

    Raises:
        TypeError: If either `a` or `b` is not an integer or a float.

    Returns:
        int: The sum of `a` and `b`.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    elif isinstance(b, float):
        b = int(b)
    
    return a + b
