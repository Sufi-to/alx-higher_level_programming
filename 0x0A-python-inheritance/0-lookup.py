#!/usr/bin/python3
def lookup(obj):
    if obj:
        return (dir(obj))


print(lookup(list))
