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

    def to_json(self, attrs=None):
        """Converts the Student object into a dictionary.

        Args:
            attrs (list of str, optional): A list of attribute names to include
                in the dictionary. If None, all attributes will be included.
                Defaults to None.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        attrs_dict = self.__dict__
        attrs_only = {}

        if attrs is None:
            return self.__dict__

        for key, value in attrs_dict.items():
            if key in attrs:
                attrs_only[key] = value
        return attrs_only
