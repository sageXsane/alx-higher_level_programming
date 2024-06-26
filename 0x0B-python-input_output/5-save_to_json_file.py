#!/usr/bin/python3
""" save_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json method:
        writes an Object to a text file, using a JSON representation

        Args:
            my_obj - python obj to be serialised to JSON saved to file
            filename - name of file storing json formatted obj
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
