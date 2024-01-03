#!/usr/bin/python3
def uppercase(str):
    strupp = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 123:
            strupp += chr(ord(i) - 32)
        else:
            strupp += i

    print("{}".format(strupp))
