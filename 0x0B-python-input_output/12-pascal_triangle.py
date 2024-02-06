#!/usr/bin/python
"""Contains the pascal_triangle function."""


def pascal_triangle(n):
    """Return list of of lists of integers that represent.
    the pascal's triangle of n.
    """
    if n <= 0:
        return []
