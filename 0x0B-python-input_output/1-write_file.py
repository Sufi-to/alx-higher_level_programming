#!/usr/bin/python3
"""Contains the write_file function."""


def write_file(file_name="", text=""):
    """Write to a text file and return the written num of bytes."""
    with open(file_name, 'w', encoding="UTF-8") as file:
        return (file.write(text))
