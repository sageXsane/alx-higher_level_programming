#!/usr/bin/python3

def no_c(my_string):
    """no_c function

    Args:
        my_string: string that may contain c's

    Returns:
        new string containing no c's
    """

    new_string = ""
    for char in my_string:
        if (char != 'c') and (char != 'C'):
            new_string = new_string + char

    return new_string
