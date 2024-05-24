#!/usr/bin/env python3
"""
Abstract base class for representing an animal
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for representing an animal.

    Attributes:
        None
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to produce the sound of the animal.

        Returns:
            str: A string representing the sound of the animal.
        """
        pass


"""
Subclass from Animal representing a dog
"""


class Dog(Animal):
    """
    Class representing a dog, inheriting from Animal.

    Attributes:
        None
    """

    def sound(self):
        """
        Produce the sound of a dog.

        Returns:
            str: The sound of a dog, which is "Bark".
        """
        return "Bark"


"""
Subclass from Animal representing a cat
"""


class Cat(Animal):
    """
    Class representing a cat, inheriting from Animal.

    Attributes:
        None
    """

    def sound(self):
        """
        Produce the sound of a cat.

        Returns:
            str: The sound of a cat, which is "Meow".
        """
        return "Meow"
