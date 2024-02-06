#!/usr/bin/python3
"""This is a module for the base class."""


class BaseGeometry:
    """This is a BaseGeometry class."""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
