#!/usr/bin/python3
"""This a "3-say_my_name" module."""


def say_my_name(first_name, last_name=""):
    """Print the a message with the first and last names."""
    if type(first_name) is type(""):
        raise TypeError("first_name must be a string")
    if type(last_name) is type(""):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
