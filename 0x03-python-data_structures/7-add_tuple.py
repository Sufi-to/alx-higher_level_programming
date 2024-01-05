#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_list1 = list(tuple_a)
    new_list2 = list(tuple_b)
    while True:
        if len(new_list1) < 2:
            new_list1.append(0)
        if len(new_list1) == 2:
            break
    while True:
        if len(new_list2) < 2:
            new_list2.append(0)
        if len(new_list2) == 2:
            break
    return new_list1[0] + new_list2[0], new_list1[1] + new_list2[1]
