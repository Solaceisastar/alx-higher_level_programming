#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    r_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    sum = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1:
            if r_dict[roman_string[i]] < r_dict[roman_string[i + 1]]:
                sum += r_dict[roman_string[i + 1]] - r_dict[roman_string[i]]
                i += 2
            else:
                sum += r_dict[roman_string[i]]
                i += 1
        else:
            sum += r_dict[roman_string[i]]
            i += 1
    return sum
