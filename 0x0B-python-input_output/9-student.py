#!/usr/bin/python
"""Contains the class Student."""


class Student:
    """This is a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve the dict represenation of Student instance."""
        json_obj = self.__dict__
        return json_obj
