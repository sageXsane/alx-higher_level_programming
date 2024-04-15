#!/usr/bin/python3
""" my list module """


class MyList(list):
    """ MyList class:
        custom list object that inherits from list
    """

    def print_sorted(self):
        """  prints the list, but sorted (ascending sort) """
        sorted_list = sorted(self)
        print(sorted_list)

    def __str__(self):
        """ str method:
            calls base classes str method
        """
        return super().__str__()
