#!/usr/bin/python3
""" add_item module """
import json
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

if not os.path.exists("add_item.json"):
    item_list = []
    save_to_json_file(item_list, "add_item.json")

if len(sys.argv) > 1:
    item_list = load_from_json_file("add_item.json")
    for arg in sys.argv[1:]:
        item_list.append(arg)
    save_to_json_file(item_list, "add_item.json")
