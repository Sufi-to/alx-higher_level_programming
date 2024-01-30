#!/usr/bin/python3
"""This is a text_identation module."""


def text_indentation(text):
    """Indent text wheneven you find the symbols."""
    if type(text) is not str:
        raise TypeError("text must be a string")
