#!/usr/bin/python3
"""this module writes a class MyList that inherits from list"""


class MyList(list):
    """subclass MyList that inherits from superclass list"""

    def __init__(self):
        """initializes the instance of the class"""

        super().__init__()

    def print_sorted(self):
        """Public instance method that prints the list,
        but sorted (ascending sort)"""

        print(sorted(self))
