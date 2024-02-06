#!/usr/bin/python3
"""This is a module for 100-my_int.py."""


class MyInt(int):
    """This is MyInt class that inherits from int."""
    def __new__(cls, *args, **kwargs):
        """Create a new instance of MyInt."""
        return (super(MyInt, cls).__new___(cls, *args, **kwargs))

    def __eq__(self, other):
        """Check if the two objects are not equal."""
        return (int(self) != other)

    def __ne__(self, other):
        """Check if the two objects are equal"""
        return (int(self) == other)


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
