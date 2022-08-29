#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    king = my_list[:]
    for count, n in enumerate(my_list):
        if n % 2 == 0:
            king[count] = True
        else:
            king[count] = False
    return (king)
