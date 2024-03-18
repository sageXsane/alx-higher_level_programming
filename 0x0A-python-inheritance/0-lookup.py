#!/usr/bin/python3
"""lookup module """


def lookup(obj):
    """ lockup method

        Lists all attributes and methods of a class/instance
        Args:
            obj: class or instance
    """
    return dir(obj)
