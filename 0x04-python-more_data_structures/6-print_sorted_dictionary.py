#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = {}
    for i in sorted(a_dictionary):
        print("{}: {}".format(i, a_dictionary[i]))
