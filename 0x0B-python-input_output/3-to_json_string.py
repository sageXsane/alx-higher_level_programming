#!/usr/bin/python3
""" to_json_string module """
import json


def to_json_string(my_obj):
    """ to_json_string method:
        returns the JSON representation of an object (string)

        Args:
            my_obj - python object to be serialized to JSON
    """
    return json.dumps(my_obj)
