#!/usr/bin/python3
"""Contains the look_up function."""


def lookup(obj):
    """Return what methods and attributes does obj have."""
    if obj:
        return (dir(obj))
