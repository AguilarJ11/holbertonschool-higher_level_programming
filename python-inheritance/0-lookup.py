#!/usr/bin/python3
"""
Lookup
"""


def lookup(obj):
    """
    Return the string representation of an object.

    Parameters:
    obj (object): The object to be represented as a string.

    Returns:
    str: The string representation of the input object.
    """
    return dir(obj)
