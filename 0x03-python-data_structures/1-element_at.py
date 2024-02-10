#!/usr/bin/python3

def element_at(my_list, idx):
    """element function - returns the element of a list at a given index

    Args:
        my_list: a list of integers
        idx: index of element

    Returns:
        The element of a list at a given index
    """

    if (idx < 0) or (idx>= len(my_list)):
        return None
    else:
        return my_list[idx]
