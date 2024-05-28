#!/usr/bin/python3

"""This module provides a class called Student to represent students."""


class Student:
    """Represents a student with their first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert the student object to a JSON-compatible dictionary.

        Returns:
            dict: A dictionary representation of the student object.
        """
        return self.__dict__
