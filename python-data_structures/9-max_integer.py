#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = len(my_list) - 1
    while i > 1:
        i2 = 0
        while i2 < i:
            if my_list[i2] > my_list[i2 + 1]:
                temp = my_list[i2]
                my_list[i2] = my_list[i2 + 1]
                my_list[i2 + 1] = temp
            i2 += 1
        i -= 1
    return my_list[-1]
