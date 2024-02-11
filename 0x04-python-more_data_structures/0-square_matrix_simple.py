#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    sq_matrix = []

    for i in range(0, len(matrix)):
        sq_numbers = list(map(lambda x: x*x, matrix[i]))
        sq_matrix.append(sq_numbers)
    return sq_matrix
