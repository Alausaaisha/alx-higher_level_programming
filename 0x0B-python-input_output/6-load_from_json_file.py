#!/usr/bin/python3
"""this modules contains a function that creates an Object
from a JSON file"""


import json


def load_from_json_file(filename):
    """method that creates an Object from a “JSON file”"""

    with open(filename, 'r', encoding="UTF8") as f:
        return(json.load(f))
