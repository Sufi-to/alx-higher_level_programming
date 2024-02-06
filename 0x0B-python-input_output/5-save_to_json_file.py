#!/usr/bin/python3
"""Contains save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Save a json object to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
