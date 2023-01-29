#!/usr/bin/python3
"""This module defines a square by:
Private instance attribute: size:property def size(self):
to retrieve it. property setter def size(self, value): to set it"""


class Square:
    """class created"""

    def __init__(self, size=0):
        """This method instantiates the class"""

        self.size = size

    @property
    def size(self):
        """this is the size attribute getter method(to retrieve size)"""

        return(self.__size)

    @size.setter
    def size(self, value):
        """this is the property setter method to set the size attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """this method returns the current square area"""

        square_area = self.__size ** 2
        return(square_area)
