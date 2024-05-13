#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for i2 in i:
            print("{:d} ".format(i2), end=" ")
    print()
