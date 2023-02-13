#!/usr/bin/python3
"""this module contains a class Base"""


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
