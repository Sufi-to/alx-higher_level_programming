#!/usr/bin/python3
"""This is a rectangle class definition."""


class Rectangle:
    """Create a rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize the width and height of the rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of rectagle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
