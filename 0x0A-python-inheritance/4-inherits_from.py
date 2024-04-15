#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """ inherits_from method:
        checks f the object is an instance of a class that
        inherited (directly or indirectly) from the specified class
        (does not include its actual class)

        Args:
            obj - object
            a_class - classs
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
