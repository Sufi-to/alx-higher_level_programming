#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big = max(a_dictionary.values())
        for key in a_dictionary.keys():
            if a_dictionary[key] == big:
                return key
    else:
        return None
