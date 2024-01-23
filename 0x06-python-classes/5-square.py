#!/usr/bin/python3
"""Class square is defined"""


class Square:
    """this is a square"""
    def __init__(self, size=0):
        """new square initialization

        Args:
                size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Sets/gets the current size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square using # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
