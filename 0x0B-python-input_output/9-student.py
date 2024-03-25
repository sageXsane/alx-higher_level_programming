#!/usr/bin/python3
""" student module
    contains of a student class that has:
        - initialises name, surname and age of student object
        - to_json method
"""


class Student:
    """ Student class:
        defines a student by name, surname and age
    """

    def __init__(self, first_name, last_name, age):
        """ init method:
            initalised class parameter to public instance attributes

            Args:
                first_name: name of student
                last_name: last name of student
                age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ to_json method:
            returns the dictionary description with simple data structure
            (list, dictionary, string, integer and boolean)
            for JSON serialization of an object
        """
        serial_dict = {}
        for key in dir(self):
            if key[0:2] != '__':
                value = getattr(self, key)
                if isinstance(value, (int, list, dict, str, bool)):
                    serial_dict[key] = value
        return serial_dict
