#!/usr/bin/python3
"""this module contains a class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square created"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiaton and initialization with the super call"""

        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    def __str__(self):
        """this method overrides the inbuilt __str__ method"""
        return("[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size))
