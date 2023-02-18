#!/usr/bin/python3
"""this module contains a class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square created"""

    def __init__(self, size, x=0, y=0, id=None):
        """instantiaton and initialization with the super call"""

        self.size = size
        super().__init__(self.size, self.size, x, y, id)

    @property
    def size(self):
        """public getter mathod for size attribute"""

        return(self.width)

    @size.setter
    def size(self, value):
        """the setter method for size attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        """this method overrides the inbuilt __str__ method"""
        return("[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.size))
