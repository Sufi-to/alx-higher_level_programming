#!/usr/bin/python3
"""Class square is defined."""


class Square:
    """this is a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
                size (int): size of the new square
                position (tuple): position of square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets/gets the current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of the square."""
        return (self.__size ** 2)

    def __eq__(self, other):
        """Check if the two circles have the same area."""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Check if the area of the two circles are not the same."""
        return (self.area() != other.area())

    def __lt__(self, other):
        """Check if the area of the first circle is < the other."""
        return (self.area() < other.area())

    def __gt__(self, other):
        """Check if the area of the first circle is > the other."""
        return (self.area() > other.area())

    def __le__(self, other):
        """Check if the area of the first cirle is <= the other circle's."""
        return (self.area() <= other.area())

    def __ge__(self, other):
        """Check if the area of the first cirle is >= the other circle's."""
        return (self.area() >= other.area())
