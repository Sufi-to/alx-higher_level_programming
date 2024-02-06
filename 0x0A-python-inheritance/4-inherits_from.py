#!/usr/bin/python3
"""Has inherits_from function."""


def inherits_from(obj, a_class):
    """return true if object is a subclass"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
