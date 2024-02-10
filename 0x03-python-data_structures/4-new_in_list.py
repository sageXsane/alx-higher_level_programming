#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """new_in_list function - replaces an element of a list at a specific position

    Args:
        my_list: integer list
        idx: index
        element: new element value

    Returns:
        new list
    """
    new_list = my_list.copy()
    if (idx >= 0) and (idx < len(my_list)):
        new_list[idx] = element

    return new_list
