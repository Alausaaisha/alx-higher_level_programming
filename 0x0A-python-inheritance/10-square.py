#!/usr/bin/python3
"""this module writes a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        """instantiates and initializes with size"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
