#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class method:
        checks if the object is an instance of or if the object is
        an instance of a class that inherited from, the specified class

        Args:
            obj: object
            a_class: class
    """
    return isinstance(obj, a_class)
