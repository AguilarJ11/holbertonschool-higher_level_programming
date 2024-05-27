#!/usr/bin/python3

"""
Method for write a file next to the last line
"""


def append_write(filename="", text=""):
    """
    Appends text to a file.

    Args:
        filename (str): The file name.
        text (str): The text to append.

    Returns:
        int: Number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
