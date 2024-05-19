#!/usr/bin/python3
"""
Square:
    A class representing a square shape.

Attributes:
    size (int): The size of the square.
    position (tuple): The position of the square.

Methods:
    __init__(self, size=0, position=(0, 0)): Initializes a new Square instance.
    area(self): Calculates the area of the square.
    my_print(self): Prints the square with '#' characters.
"""


class Square:
    """
    A class named Square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        The size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Sets the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """
        The position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Sets the position of the square.

        Args:
            position (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(position, tuple) or len(position) != 2 \
                or not isinstance(position[0], int) or not isinstance(position[1], int) \
                    or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with '#' characters.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for t in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
