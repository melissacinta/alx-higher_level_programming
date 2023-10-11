#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_array = []
        for i in matrix:
            new_array.append(list(map(lambda x:  x**2, i)))
        return new_array
