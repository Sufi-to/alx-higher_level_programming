#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        ln = 0
        for i in range(x):
            print(my_list[i], end="")
            ln += 1
        print()
    except IndexError:
        print()
    return ln
