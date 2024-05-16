#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    elem_num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]))
            elem_num += 1
        except IndexError:
            break
    print()
    return elem_num
