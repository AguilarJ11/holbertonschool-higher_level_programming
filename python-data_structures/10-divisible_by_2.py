#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    for i in my_list:
        div_list = ""
        if i % 2 == 0:
            div_list[i] = True
        else:
            div_list[i] = False
    return div_list
