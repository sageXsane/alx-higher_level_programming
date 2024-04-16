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

    def to_json(self):
        """ to_json method:
            calls class_to_json method to
            retrieves a dictionary representation of a Student instance
        """
        return class_to_json(self)
