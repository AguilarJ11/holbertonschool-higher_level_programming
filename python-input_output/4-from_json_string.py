#!/usr/bin/python3

"""
converts a JSON-formatted string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        Any: A Python object representing the JSON data.
    """
    return json.loads(my_str)
