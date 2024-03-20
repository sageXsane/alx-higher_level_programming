#!/usr/bin/python3
""" my_list module """


class MyList(list):
    """ MyList class
        Inherits list methods/attributes
    """

    def print_sorted(self):
        """ print_sorted method:
            Sorts the mylist object
        """

        sort_list = sorted(self)
        print(sort_list)

    def __str__(self):
        """__str___ method
        Displays nothing
        """

        return "[" + ", ".join(map(str, self)) + "]"