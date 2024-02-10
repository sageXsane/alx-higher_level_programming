#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print list integer function

    Args:
        my_list: a list containing integers
    """
    for i in range(0, len(my_list)):
        print("{}".format(my_list[i]))
