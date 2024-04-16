#!/usr/bin/python3
""" student module """
class_to_json = __import__('8-class_to_json').class_to_json


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
        if isinstance(attrs, list):
            if all(isinstance(elem, str) for elem in attrs):
                for key in attrs:
                    if hasattr(self, key):
                        value = getattr(self, key)
                        if isinstance(value, (list, dict, str, int, bool)):
                            json_dict[key] = value
        else:
            json_dict = class_to_json(self)
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
