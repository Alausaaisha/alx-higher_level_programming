#!/usr/bin/python3
"""this module contains a script that adds all arguments to a
Python list, and then save them to a file"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    pyt_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pyt_list = []
pyt_list.extend(sys.argv[1:])
save_to_json_file(pyt_list, "add_item.json")
