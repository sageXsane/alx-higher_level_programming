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

    def to_json(self, attrs=None):
        """ to_json method:
            returns the dictionary description with simple data structure
            (list, dictionary, string, integer and boolean)
            for JSON serialization of an object

            Args:
                attrs: list of strings containing attribute keys
                        to be serialised
        """
        serial_dict = {}
        lst = []
        if attrs is None or not all(isinstance(elem, str) for elem in attrs):
            attrs = dir(self)
        for key in attrs:
            if key[0:2] != '__' and key in dir(self):
                value = getattr(self, key)
                if isinstance(value, (int, list, dict, str, bool)):
                    serial_dict[key] = value
        return serial_dict

    def reload_from_json(self, json):
        """ reload_from_json method:
            replaces all attributes of the Student instance

            Args:
                json: dict containing new attribute values
        """
        for key in list(json.keys()):
            if key in dir(self):
                setattr(self, key, json[key])
