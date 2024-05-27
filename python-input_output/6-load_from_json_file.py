#!/usr/bin/python3

"""
Loads a Python object from a JSON file.
"""

import json



def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load the object from.

    Returns:
        Any: The Python object loaded from the JSON file.

    The function reads the JSON data from the specified file and deserializes it into a Python object.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
