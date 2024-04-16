#!/usr/bin/python3
""" from_json_string module """
import json


def from_json_string(my_str):
    """ from_json_string method:
        returns a python object represented by a JSON string

        Args:
            my_str - json string to be deserialised to python data object
    """
    return json.loads(my_str)
