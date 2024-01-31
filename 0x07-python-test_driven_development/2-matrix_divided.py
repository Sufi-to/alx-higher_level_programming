#!/usr/bin/python3
"""This is a "2-matrix_divided" module."""


def matrix_divided(matrix, div):
    """Return a matrix divided by "div"."""
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        for j in i:
            if type(j) not in (int, float):
                raise TypeError
            ("""matrix must be a matrix (list of lists) of integers/floats""")
    len_i = len(matrix[0])
    for i in matrix:
        if len_i != len(i):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(element/div, 2) for element in row] for row in matrix]
