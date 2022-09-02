#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == [] or my_list is None:
        return (0)
    king = 0
    queen = 0
    for x, y in my_list:
        king += x * y
        queen += y
    return (king / queen)
