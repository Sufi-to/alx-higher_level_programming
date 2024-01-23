#!/usr/bin/python3
"""Import math module."""
import math


"""MagicClass class defined."""


class MagicClass:
    """This is a MagicClass."""

    def __init__(self, radius=0):
        """Initialize a circle radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number.")
        self.__radius = radius

    def area(self):
        """Return area of circle."""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Return circumference of circle."""
        return (self.__radius * 2 * math.pi)
