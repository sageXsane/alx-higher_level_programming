#!/usr/bin/python3
""" say my name module
    Has one function called say_my_name -
    displays the given name and surname
"""


def say_my_name(first_name="", last_name=""):
    """ say_my_name function:

        prints the name and surname given in a related message

        Args:
            first_name: string value representing the name of a person
            last_name: string representing the surname of a person (optional)

        Expections:
            TypeError: first_name must be a string or
                    last_name must be a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

    if __name__ == "__main__":
        import doctest
        doctest.testmod(Verbose=True)
