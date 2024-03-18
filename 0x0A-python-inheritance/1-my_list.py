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
        self.sort()
        print(self)
