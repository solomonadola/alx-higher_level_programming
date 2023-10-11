#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weighted = 0
    div = 0
    for el in my_list:
        weighted += el[0] * el[1]
        div += el[1]
    return weighted/div
