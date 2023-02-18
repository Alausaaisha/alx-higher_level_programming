#!/usr/bin/python3
"""this module contains a class Base"""


import json


class Base:
    """class created"""

    __nb_objects = 0

    def __init__(self, id=None):
        """method instantiates and initializes with id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation
        of list_dictionaries"""

        if list_dictionaries is None:
            return("[]")
        else:
            return(json.dumps(list_dictionaries))
