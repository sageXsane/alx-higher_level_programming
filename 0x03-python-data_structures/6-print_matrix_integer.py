#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """print_matrix_integer

    Args:
        matrix: a matrix of integers
    """
    for row in range(0, len(matrix)):
        last = len(matrix[row])
        for col in range(0, last):
            print("{:d}".format(matrix[row][col]), end="")
            if (col != last - 1):
                print(end=" ")
        print(end="\n")
