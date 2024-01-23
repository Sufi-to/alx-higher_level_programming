#!/usr/bin/python3
"""Class square is defined"""


class Square:
    """this is a square"""
    def __init__(self, size=0):
        """new square initialization

        Args:
                size (int): size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns area of the square"""
        return (self.__size * self.__size)
