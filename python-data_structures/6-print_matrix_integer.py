#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        last = 0
        for i2 in i:
            if len(i) - 1 == last:
                print("{:d}".format(i2), end="")
            else:
                print("{:d}".format(i2), end=" ")
                last += 1
        print()
