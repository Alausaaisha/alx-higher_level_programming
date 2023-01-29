#!/usr/bin/python3
"""This module defines a class Square by:
    Private instance attribute: size"""


class Square:
    """class Square created"""

    def __init__(self, __size=0):
        """This method instantiates class with size"""

        self.__size = __size
        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This method returns the current square area"""

        square_area = self.__size**2
        return(square_area)
