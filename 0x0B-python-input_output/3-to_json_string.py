#!/usr/bin/python3
"""Contains to_json_string function."""


import json


def to_json_string(my_obj):
    """Return json representation of an object."""
    return json.dumps(my_obj)
