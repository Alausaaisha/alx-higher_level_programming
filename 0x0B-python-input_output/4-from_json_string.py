#!/usr/bin/python3
"""the module contains a function that returns an object
(Python data structure) represented by a JSON string"""


import json


def from_json_string(my_str):
    """this methods returns an object represented by a JSON string"""

    return(json.loads(my_str))
