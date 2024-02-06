#!/usr/bin/python3
"""This is a module for the subclass rectangle and
baseGeometry class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a square class that inherits from rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)
