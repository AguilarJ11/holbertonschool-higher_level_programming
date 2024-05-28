#!/usr/bin/python3

import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arg = sys.argv[1:]

add_arg = []

for i in arg:
        add_arg.append(i)
try:
    add_arg = load_from_json_file("add_item.json")
    save_to_json_file(add_arg, "add_item.json")
except:
    save_to_json_file(add_arg, "add_item.json")