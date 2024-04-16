#!/usr/bin/python3
""" 8-class_to_json module """


def class_to_json(obj):
    """ class_to_json method:
        returns the dictionary description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object

        Args:
            obj - class object
    """
    json_dict = {}
    for key in dir(obj):
        if key[0:2] != '__':
            value = getattr(obj, key)
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
    return json_dict
