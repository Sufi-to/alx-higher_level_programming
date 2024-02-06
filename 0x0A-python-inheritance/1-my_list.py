#!/usr/bin/python3
"""This is a list module."""


class MyList(list):
    """This is MyList class."""
    def __init__(self):
        """Initialize self from parent class."""
        super().__init__()

    def print_sorted(self):
        """Print the list in a sored way."""
        num_sorted = sorted(self)
        print(num_sorted)
