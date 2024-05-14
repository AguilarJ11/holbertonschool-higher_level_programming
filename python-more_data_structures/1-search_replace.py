#!/usr/bin/python3

def search_replace(my_list, search, replace):
    pos = 0
    new_list = my_list[:]
    for i in my_list:
        if i == search:
            pos = new_list.index(i, pos)
            new_list[pos] = replace
            pos += 1
    return new_list
