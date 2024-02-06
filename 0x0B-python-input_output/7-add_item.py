#!/usr/bin/python3
"""Contains the function save_to_json_file."""


from sys import argv
import json
from pathlib import Path


def load_from_json_file(filename):
    """Create a python object from a json file."""
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline().strip()
        return json.loads(line)


def save_to_json_file(my_obj, filename):
    """Save a json object to a file."""
    x = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(x)


if __name__ == "__main__":
    """Run this file only when __name__ = main."""
    data_from_json_file = []
    filename = "add_item.json"
    if len(argv) == 1 and (not Path(filename).exists()):
        save_to_json_file(data_from_json_file, filename)
    if len(argv) > 1:
        data_from_json_file = load_from_json_file(filename)
        for i in range(1, len(argv)):
            data_from_json_file.append(argv[i])
        save_to_json_file(data_from_json_file, filename)
