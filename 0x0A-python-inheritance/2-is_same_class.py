#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """ is_same_class method:
        returns True if the object is exactly an instance of the
        specified class otherwise False

        Args:
            obj: object
            a_class: class
    """
    return type(obj) is a_class
