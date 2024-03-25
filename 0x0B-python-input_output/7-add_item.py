#!/usr/bin/python3
""" add_item module """
import json
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if not os.path.exists("add_item.json"):
    em_list = []
    with open("add_item.json", 'w', encoding="utf-8") as f:
        json.dump(em_list, f)

if len(sys.argv) > 1:
    with open("add_item.json", "r+") as f:
        item_list = json.load(f)
        for arg in sys.argv[1:]:
            item_list.append(arg)
        f.seek(0)
        f.truncate()
        json.dump(item_list, f)
