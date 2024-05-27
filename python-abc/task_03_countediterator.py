#!/usr/bin/env python3

"""
A Class that counts the number of items iterated
"""


class CountedIterator:
    """
    A Class that counts the number of items iterated over.

    Attributes:
        iterator (iterator): The internal iterator.
        iter_count (int): The count of iterated items.
        iter_len (int): The length of the iterable.
    """

    def __init__(self, iter_obj):
        """
        Initializes with an iterable object.

        Args:
            iter_obj (iterable): An iterable object.
        """
        self.iterator = iter(iter_obj)
        self.iter_count = 0
        self.iter_len = len(iter_obj)

    def get_count(self):
        """
        Returns the number of items iterated over.

        Returns:
            int: The count of iterated items.
        """
        return self.iter_count

    def __next__(self):
        """
        Returns the next item and increments the count.

        Raises:
            StopIteration: If the iterator is exhausted.
        """
        if self.iter_count < self.iter_len:
            self.iter_count += 1
            return next(self.iterator)
        else:
            raise StopIteration
