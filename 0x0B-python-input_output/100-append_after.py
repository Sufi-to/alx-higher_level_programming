#!/usr/bin/python
"""Contains the append_after function."""


def append_after(filename="", search_string="",
                 new_string=""):
    """Insert a line of text to a file after a particular string."""
    read_file = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            read_file += [line]
            if line.find(search_string) != -1:
                read_file += [new_string]

    with open(filename, 'w', encoding='utf-8') as file:
        file.write("".join(read_file))
