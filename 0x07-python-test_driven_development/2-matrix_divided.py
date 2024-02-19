#!/usr/bin/python3

""" matrix divided module

    divides each element of a int/float list of lists by a common divisor
"""


def matrix_divided(matrix, div):
    """ matrix_divided function

        divides each element of a matrix by a divisor
        Args:
        matrix: an integer/float list of lists
        div: common divisor

        Return: returns a new matrix with elements being the result of
        the division of the correspponding values of the old matrix

        Exceptions:
        TypeError: if div is not a number or None
                    if values of matrix are not an int/float
                    if each row of list is not the same size
        ZeroDivisionError: if div is zero

    """

    div_matrix = []

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            TypeError("matrix must be a matrix (list of lists) \
                      of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        div_row = []
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                                integers/floats")
            div_row.append(round(elem / div, 2))
        div_matrix.append(div_row)
    return div_matrix


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
