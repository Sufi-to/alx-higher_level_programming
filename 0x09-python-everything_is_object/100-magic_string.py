#!/usr/bin/python3
def magic_string():
    global i
    return ("BestSchool, " * (i := i + 1))[:-2]
