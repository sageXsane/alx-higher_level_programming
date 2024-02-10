#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replace_in_list function - replaces an element of a list at a specific position

    Args:
        my_list: integer list
        idx: index
        element: new element value

    Returns:
        edited list
    """

    if (idx >= 0) and (idx < len(my_list)):
        my_list[idx] = element

    return my_list
