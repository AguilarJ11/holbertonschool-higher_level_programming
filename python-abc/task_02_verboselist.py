#!/usr/bin/env python3

"""
A subclass of list
"""


class VerboseList(list):
    """
    A subclass of list that provides verbose messages for list operations.
    """

    def append(self, value):
        """
        Append a value to the end of the list.

        Args:
            value: The value to append to the list.
        """
        super().append(value)
        print(f"Added [{value}] to the list.")

    def extend(self, value):
        """
        Extend the list by appending elements from the iterable.

        Args:
            value: An iterable whose elements will be appended to the list.
        """
        super().extend(value)
        print(f"Extended the list with [{len(value)}] items")

    def remove(self, value):
        """
        Remove the first occurrence of a value from the list.

        Args:
            value: The value to remove from the list.
        """
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, value=None):
        """
        Remove and return the last item in the list, or remove and return
        an item at the specified index.

        Args:
            value (optional): If specified, the index of the item to remove.
                Defaults to None, in which case the last item is removed.

        Returns:
            The removed item.
        """
        if value is None:
            print(f"Popped [{self[-1]}] from the list.")
            super().pop()
            
        else:
            print(f"Popped [{self[value]}] from the list.")
            super().pop(value)
