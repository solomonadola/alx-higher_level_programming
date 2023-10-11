#!/usr/bin/python3

def uniq_add(my_list=[]):
    temp_list = []
    sum = 0
    for el in my_list:
        if el not in temp_list:
            temp_list.append(el)
            sum += el
    return sum
