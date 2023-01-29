#!/usr/bin/python3
"""This module defines a class Square by private
instance attribute: size """


class Square:
    """The class Square"""

    def __init__(self, __size=0):
        """This method instantiates the class with size"""

        self.__size = __size

        if not isinstance(__size, int):
            raise TypeError("size must be an integer")
        elif __size < 0:
            raise ValueError("size must be >= 0")
