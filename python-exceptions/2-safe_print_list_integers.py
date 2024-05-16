#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_print = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
        except (TypeError, ValueError):
            continue
    print()
    return num_print
