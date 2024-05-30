#!/usr/bin/python3

"""
A module to create, serialize, and deserialize objects.
"""

import pickle


class CustomObject:
    """
    Represents a custom object with name, age, and student status.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the CustomObject with name, age, and student status.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Indicates if the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the details of the CustomObject."""

        print(f"Name: {self.name}\nAge: {self.age}\n\
            Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object to a file.

        Parameters:
        filename (str): The name of the file to save the object to.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes the object from a file.

        Parameters:
        filename (str): The name of the file to load the object from.

        Returns:
        CustomObject: The deserialized CustomObject,
        None if deserialization fails.
        """

        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
