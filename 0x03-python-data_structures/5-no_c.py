#!/usr/bin/python3

def no_c(my_string):
    out = ''
    for c in my_string:
        if c not in "cC":
            out += c
    return out
