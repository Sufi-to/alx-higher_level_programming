#!/usr/bin/python3
"""Contains the function load_from_json_file."""


import json


def load_from_json_file(filename):
    """Create a python object from a json file."""
    with open(filename, "r", encoding="utf-8") as file:
        line = file.readline().strip()
        return json.loads(line)
