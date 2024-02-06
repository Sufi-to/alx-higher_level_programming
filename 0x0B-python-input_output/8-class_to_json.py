#!/usr/bin/python3
"""Contains the class_to_json function."""


def class_to_json(obj):
    """Convert a class to json representation."""
    json_obj = obj.__dict__
    return json_obj
