#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500}
    if not isinstance(roman_string, str):
        return 0
    result = 0
    num = 0
    num_ant = 0
    for c in roman_string:
        num = roman_numbers[c]
        if num_ant == 0:
            result += num
        elif num > num_ant:
            result += num
        else:
            result -= num_ant
        num_ant = num
    return result
