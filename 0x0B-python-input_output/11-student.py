#!/usr/bin/python3
""" student module """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ init method:
            initialises public instance attributes:
                - first_name
                - last_name
                - age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to_json method:
            calls class_to_json method to
            retrieves a dictionary representation of a Student instance
        """
        json_dict = {}
        attr_lst = []
        if isinstance(attrs, list):
            if all(isinstance(elem, str) for elem in attrs):
                attr_lst = attrs
        else:
            attr_lst = dir(self)
        for key in attr_lst:
            if hasattr(self, key) and key[0:2] != '__':
                value = getattr(self, key)
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[key] = value
        return json_dict

    def reload_from_json(self, json):
        """ reload_from_json method:
             replaces all attributes of the Student instance

             Args:
                json - dictionary representation of class attributes
        """
        for key in list(json.keys()):
            if hasattr(self, key):
                setattr(self, key, json[key])
