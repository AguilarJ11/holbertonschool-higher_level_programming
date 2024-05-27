#!/usr/bin/python3


"""
Method for read a file
"""


def read_file(filename=""):
    """
    Reads and prints the content of a file.

    Args:
        filename (str): The path to the file to be read.
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
