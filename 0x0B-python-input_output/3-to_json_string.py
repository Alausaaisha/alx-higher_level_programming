#!/usr/bin/python3
"""this module contains a function that returns the JSON
representation of an object (string)"""

import json


def to_json_string(my_obj):
    """this method returns the JSON representation of an object"""

    return(json.dumps(my_obj))
