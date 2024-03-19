#!/usr/bin/python3
""" inherits_from  module """


def inherits_from(obj, a_class):
    """ inherits_from method:
        Checks whether object is an instance of a class that inherited
        (directly or indirectly) from the specified class

        Args:
            obj: object
            a_class: class
        Returns:
            True if the class the object belongs to is a subclass of a_class
            else False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
