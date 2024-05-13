#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for i2 in i:
            if len(i) - 1 == i2:
                print("{:d}".format(i2), end="")
            else:
                print("{:d}".format(i2), end=" ")
        print()
