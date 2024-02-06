#!/usr/bin/python3
"""Module for add_attribute."""


def add_attribute(obj, att_name, att_value):
    """Add an attribute to a class."""
    if not hasattr(obj, "__dict__"):
        raise TypeError('can\'t add new attribute')
    if (not hasattr(obj, att_name)):
       obj.__setattr__(att_name, att_value)
