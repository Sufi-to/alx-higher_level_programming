#!/usr/bin/python3
"""Contains save_to_json_file function."""


import json


def save_to_json_file(my_obj, filename):
    """Save a json object to a file."""
    x = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(x)
