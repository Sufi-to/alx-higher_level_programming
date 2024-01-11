#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    roman_n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num_ls = [roman_n[i] for i in roman_string]
    if len(num_ls) == 1:
        return num_ls[0]
    num = 0
    for x in range(len(num_ls)-1):
        if num_ls[x] >= num_ls[x + 1]:
            num += num_ls[x]
        else:
            num -= num_ls[x]
    if num_ls[-1] >= num_ls[-2]:
        num += num_ls[-1]
    else:
        num -= num_ls[-1]

    return num
