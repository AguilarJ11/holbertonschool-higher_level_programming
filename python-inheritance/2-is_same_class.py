#!/usr/bin/python3
"""
Check if an objetct belongs to a specific class
"""


def is_same_class(obj, a_class):
    """
    Check if an object belongs to a specific class.

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to compare against.

    Returns:
    bool: True if the object belongs to the specified class, False otherwise.
    """
    return True if isinstance(obj, a_class) else False
