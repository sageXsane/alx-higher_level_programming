#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """print_reversed_list_integer

    Args:
        my_list = integer list
    """
    if my_list is not None:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
