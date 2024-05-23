#!/usr/bin/python3

class MyList(list):
    """Subclass of list with a method to print its elements sorted.

    Args:
        list: Base class providing a mutable list of objects.

    Methods:
        print_sorted(): Prints the elements of the list in ascending order.
    """

    def print_sorted(self):
        """Prints the elements of the list in ascending order."""
        print(sorted(self))
