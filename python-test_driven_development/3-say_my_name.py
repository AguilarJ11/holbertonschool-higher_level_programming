#!/usr/bin/python3
"""
Print the full name
"""


def say_my_name(first_name, last_name=""):
    """
    Print the full name

    Parameters:
        first_name (str)
        last_name (str)

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Examples:
        >>> say_my_name("John", "Doe")
        My name is John Doe

        >>> say_my_name("Jane")
        My name is Jane
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
