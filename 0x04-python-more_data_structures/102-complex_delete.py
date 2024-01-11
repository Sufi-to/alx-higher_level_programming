#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [key for key in a_dictionary if a_dictionary[key] == value]
    for x in keys:
        del a_dictionary[x]

    return a_dictionary
