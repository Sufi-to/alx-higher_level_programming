#!/usr/bin/python3
"""This is a text_identation module."""


def text_indentation(text):
    """Indent text wheneven you find the symbols."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    spl = [":", "?", "."]
    new_str = ""
    for i in text:
        if i in spl:
            new_str += i
            print(new_str)
            print()
            new_str = ""
        else:
            new_str += i
