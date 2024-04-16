#!/usr/bin/python3
""" load_from_json_file module """
import json


def load_from_json_file(filename):
    """ load_from_json_file method:
        creates an Object from a “JSON file”

        Args:
            filename: name of file that reads json formatted obj
    """
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
