#!/usr/bin/env python3


"""
A mixin class with the swim function
"""


class SwimMixin:
    """A mixin class that provides swimming functionality."""

    def swim(self):
        """Makes the creature swim."""
        print("The creature swims!")


"""
A mixin class with the fly function
"""


class FlyMixin:
    """A mixin class that provides flying functionality."""

    def fly(self):
        """Makes the creature fly."""
        print("The creature flies!")


"""
A Dragon class inhereits from Swim and Fly mixins
"""


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim and fly."""

    def roar(self):
        """Makes the dragon roar."""
        print("The dragon roars!")
