#!/usr/bin/python3

import os


"""
Method for read a file
"""


def read_file(filename=""):
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
