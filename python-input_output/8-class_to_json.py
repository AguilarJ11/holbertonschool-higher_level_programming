#!/usr/bin/python3

"""
 Returns a dictionary representation of an object
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of an object's instance attributes.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary of the object's instance attributes.
    """
    return obj.__dict__
