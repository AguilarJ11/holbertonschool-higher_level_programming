#!/usr/bin/python3

def roman_to_int(roman_string):
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                     'D': 500}
    suma = 0
    for i in roman_string:
        i2 = 0
        for i2 in roman_numbers:
            if i == i2:
                suma += roman_numbers.get(i2)
    return suma
