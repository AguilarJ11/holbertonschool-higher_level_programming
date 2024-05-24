#!/usr/bin/python3
"""
Check if an objetct belongs to a specific class or subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object belongs to a specific class or subclass.

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to compare against.

    Returns:
    bool: True if the object belongs to the specified class or 
    subclass, False otherwise.
    """
    return True if isinstance(obj, a_class) else False
