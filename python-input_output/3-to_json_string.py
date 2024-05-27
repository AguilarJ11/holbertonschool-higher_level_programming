#!/usr/bin/python3


"""
Representation of an objetc in JSON format
"""
import json


def to_json_string(my_obj):
    """Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: A JSON-formatted string representing the input object.
    """
    return json.dumps(my_obj)
