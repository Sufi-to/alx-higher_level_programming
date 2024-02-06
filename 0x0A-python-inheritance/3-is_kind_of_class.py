#!/usr/bin/python3
"""Contains the is_kind_of_class function."""


def is_kind_of_class(obj, a_class):
    """Return true if obj is instance of a_class."""
    return (True if isinstance(obj, a_class) else False)
