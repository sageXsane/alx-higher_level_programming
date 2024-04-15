#!/usr/bin/python3
""" add_attribute module"""


def add_attribute(a_class, attribute, value):
    """ add_attribute method:
        adds a new attribute to an object if it’s possible
        (only to custom classes and not builtin ones)

        Args:
            a_class: class name
            attribute: atrribute
            value: attribute value
    """
    if isinstance(a_class, (int, float, str, list, dict, tuple, set)):
        raise TypeError("can't add new attribute")
    elif '__slots__' in dir(a_class):
        raise TypeError("can't add new attribute")
    elif attribute in dir(a_class):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, attribute, value)
