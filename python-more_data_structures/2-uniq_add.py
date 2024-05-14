#!/usr/bin/python3

def uniq_add(my_list=[]):
    suma = 0
    for i in my_list:
        if my_list.count(i) == 1:
            suma += 1
    return suma
