#!/usr/bin/python3
"""
Defines a simple rectangle class.
"""


class Rectangle:
    """
    A class representing a rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        return 0 if self.width == 0 or self.height == 0 \
            else 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle with '#'
        """
        rec_print = ""
        for t in range(self.height):
            rec_print += str(self.print_symbol) * self.width + '\n'
        rec_print = rec_print[:-1]
        return "" if self.height == 0 or self.width == 0 else rec_print

    def __repr__(self):
        """
        Return a string representing the instance.

        Returns:
            str: A string representing the current instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Destructor method. Called when an instance of Rectangle is deleted.
        Decrements the number_of_instances class attribute.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two rectangles and return the one with
        the greater or equal area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the greater or equal area.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new square Rectangle instance.

        Args:
            cls (class): The class itself.
            size (int): The size of the square. Default is 0.

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return cls(size, size)
