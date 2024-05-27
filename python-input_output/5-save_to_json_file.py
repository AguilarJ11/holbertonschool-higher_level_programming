#!/usr/bin/python3

"""
Saves a Python object to a file using JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a file using JSON.

    Args:
        my_obj: The Python object to be saved.
        filename (str): The name of the file to save the object to.

    The function serializes the Python object to JSON format
    and writes it to the specified file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
