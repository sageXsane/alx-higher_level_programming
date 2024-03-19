#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """ is_same_class method
        Checks whether an object is an exact instance of a class

        Args:
            obj: object
            a_class: class
        Returns:
            True if obj is instance of a_class else False
    """
    return type(obj) is a_class
