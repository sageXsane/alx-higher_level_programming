#!/usr/bin/python3
""" class to json module """
import json


def class_to_json(obj):
    """ class_to_json method:
        returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
    """
    serial_dict = {}
    for key in dir(obj):
        if key[0:2] != '__':
            value = getattr(obj, key)
            if isinstance(value, (int, list, dict, str, bool)):
                serial_dict[key] = value
    return serial_dict
