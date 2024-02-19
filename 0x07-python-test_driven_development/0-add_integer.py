#!/usr/bin/python3
""" add_integer module

    contains a function called add_integer that returns the sum of two integers
"""


def add_integer(a, b=98):
    """ add_integer functions

        Adds two casted int numbers( which are originally int or float)
        Args:
        a: first number
        b: second number

        Return: returns the sum of a and b

        Exceptions: TypeError when a and b are not integer/float values
    """
    if a != a:
        a = 89
    if b != b:
        b = 89

    if not isinstance(a, (int, float)) or (a is None):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)) or (b is None):
        raise TypeError("b must be an integer")
    else:
        result = a + b
        if result == float('inf') or result == -float('inf'):
            return 89
        else:
            return int(result)
