#!/usr/bin/python3
""" say my name module """

def say_my_name(first_name, last_name=""):
    """ say_my_name method:
        prints My name is <first name> <last name>

        Args:
            first_name - first name
            last_name - surname
        Exceptions:
            TypeError: if first name/ last name are not strings
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
