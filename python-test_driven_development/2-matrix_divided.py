#!/usr/bin/python3

def matrix_divided(matrix, div):
    r_lenght = 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    for row in matrix:
        if len(row) != r_lenght and r_lenght!= 0:
            raise TypeError("Each row of the matrix must have the same size")
        r_lenght = len(row)
        for i in row:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

     return list(map(lambda x: round(x / div, 2), matrix))
