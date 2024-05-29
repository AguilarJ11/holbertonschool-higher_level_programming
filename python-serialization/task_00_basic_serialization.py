#!/usr/bin/python3

"""
module that adds the functionality to serialize a Python
dictionary to a JSON file and deserialize the JSON file
to recreate the Python Dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python object to a JSON formatted string and save it to a file.

    Parameters:
    data (any): The Python object to be serialized.
    filename (str): The name of the file where the data will be saved.

    Returns:
    None
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(data))


def load_and_deserialize(filename):
    """
    Load data from a file and deserialize it from
    a JSON formatted string to a Python object.

    Parameters:
    filename (str): The name of the file to load the data from.

    Returns:
    any: The deserialized Python object.
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
