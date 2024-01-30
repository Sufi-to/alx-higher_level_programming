#!/usr/bin/python3
def magic_string(static=[0]):
    static[0] += 1
    return ("BestSchool, " * static[0])[:-2]
