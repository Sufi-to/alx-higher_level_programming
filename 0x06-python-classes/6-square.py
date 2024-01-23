#!/usr/bin/python3
"""Class square is defined"""


class Square:
    """this is a square"""
    def __init__(self, size=0, position=(0, 0)):
        """new square initialization

        Args:
                size (int): size of the new square
                position (tuple): position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Sets/gets the current size of square"""
        return (self.__size)

    @property
    def position(self):
        """Set/get teh current position of square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                not all(isinstance(x, int) for x in value) or
                len(value) != 2 or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
