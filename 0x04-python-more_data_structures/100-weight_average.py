#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        total = 0
        to_add = 0
        add = list(map(lambda x: x[1], my_list))
        for i in add:
            to_add += i
        mult = list(map(lambda x: x[0] * x[1], my_list))
        for i in mult:
            total += i

        return total/to_add
    else:
        return 0
