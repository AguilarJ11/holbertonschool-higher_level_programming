#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num_print = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num_print += 1
        except IndexError:
            break
        except (TypeError, ValueError):
            continue
    print()
    return num_print
