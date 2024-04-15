#!/usr/bin/python3
""" MyInt module """


class MyInt(int):
    """ MyInt class:
        custom int class that inheirts from int
    """

    def __eq__(self, value: object):
        """ rebel __eq__ method:
            inverts from super class method

            Returns:
                True: if condition is false
                False: if condition is true
        """
        return not (super().__eq__(value))

    def __ne__(self, value: object) -> bool:
        """ rebel __ne__ method:
            inverts from super class method

            Returns:
                True: if objects are equal
                False: if objects are not equal
        """
        return not (super().__ne__(value))
