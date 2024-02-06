#!/usr/bin/python3
"""Contains append_write function."""


def append_write(file_name="", text=""):
    """Append text to the end of file."""
    with open(file_name, "a", encoding="utf-8") as file:
        return file.write(text)
