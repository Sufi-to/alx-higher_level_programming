#!/usr/bin/python3
"""This module containes the read_file function."""


def read_file(filename=""):
    """Read file and print to stdout."""
    with open(filename, encoding="UTF-8") as file:
        print(file.read(), end="")
