#!/usr/bin/python3

"""
Method for write a file
"""


def write_file(filename="", text=""):
    """
    Write the specified text to a file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    """
    with open(filename, mode="w", encoding="utf-8") as f:
       return f.write(text)
