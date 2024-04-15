#!/usr/bin/python3
""" add_attribute module"""


def add_attribute(inst, attribute, value):
    """ add_attribute method:
        adds a new attribute to an object if it’s possible
        (only to custom classes and not builtin ones)

        Args:
            inst: object instance
            attribute: atrribute
            value: attribute value
    """
    if not hasattr(inst, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(inst, attribute, value)
