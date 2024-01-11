#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    x = 0
    for i in my_set:
        x = x + i

    return x
