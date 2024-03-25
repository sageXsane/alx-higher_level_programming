#!/usr/bin/python3
""" load_from_json_file """
import json


def load_from_json_file(filename):
    """ load_from_json_file method:
        creates an Object from a “JSON file”
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
