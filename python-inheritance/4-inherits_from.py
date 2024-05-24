#!/usr/bin/python3
"""
Check if an object inherits from a specific class
"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Parameters:
    obj (object): The object to be checked.
    a_class (class): The class to compare against.

    Returns:
    bool: True if the object belongs to the specified class, False otherwise.
    """
    return True if issubclass(type(obj), a_class) \
        and type(obj) is not a_class else False
