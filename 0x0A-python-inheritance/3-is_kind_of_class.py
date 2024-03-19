#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class method
        Checks whether  if the object is an instance of,
        or if the object is an instance of a class that inherited from
        the specified class

        Args:
            obj: object
            a_class: class
        Returns:
            True if obj is instance of a_class else False
    """
    return isinstance(obj)
