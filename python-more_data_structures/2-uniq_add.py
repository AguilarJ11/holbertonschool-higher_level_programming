#!/usr/bin/python3

def uniq_add(my_list=[]):
    suma = 0
    new_list = my_list[:]
    for i in new_list:
        if len(new_list) == 1:
            return i
        if new_list.count(i) > 1:
            new_list.remove(i)
    for i in new_list:
        if new_list.count(i) == 1:
            suma += i
    return suma
