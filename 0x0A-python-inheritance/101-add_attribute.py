#!/usr/bin/python3
def add_attribute(obj, att_name, att_value):
    if att_name in obj.__dict__.keys():
        raise TypeError('can\'t add new attribute')
    else:
       obj.att_name = att_value


