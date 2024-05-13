#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        copy_my_list = my_list[:]
        copy_my_list[idx] = element
        return copy_my_list
