#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = []
    for (key, val) in a_dictionary.items():
        if value == val:
            keys.append(key)
    for key in keys:
        del a_dictionary[key]
    return a_dictionary
