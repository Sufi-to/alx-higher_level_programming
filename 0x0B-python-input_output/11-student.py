#!/usr/bin/python3
"""Contains the Student class."""


class Student:
    """This is a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student object."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve the dict represenation of Student instance."""
        if attrs is None:
            json_obj = self.__dict__.copy()
            return json_obj
        else:
            new_obj = {}
            for i in attrs:
                if i in self.__dict__:
                    new_obj[i] = self.__dict__[i]
            return new_obj

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance."""
        self.first_name = json['first_name']
        self.last_name = json['last_name']
        self.age = json['age']
