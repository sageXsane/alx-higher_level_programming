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
    if not isinstance(type(a_class), type):
        raise TypeError("can't add new attribute")
    if isinstance(a_class, (int, float, str, tuple)):
        raise TypeError("can't add new attribute")
    elif '__slots__' in dir(a_class) or not hasattr(a_class, "__dict__"):
        raise TypeError("can't add new attribute")
    elif hasattr(a_class, attribute):
        raise TypeError("can't add new attribute")
    else:
        setattr(a_class, attribute, value)
