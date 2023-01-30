#!/usr/bin/python3
"""this module defines a class Square and defines a public instsnce
method that prints in stdout the square with the character #"""


class Square:
    """class created"""

    def __init__(self, size=0):
        """this method instantiates the class"""

        self.size = size

    @property
    def size(self):
        """this method retrieves the value of attribute size"""

        return(self.__size)

    @size.setter
    def size(self, value):
        """this method sets the value of attribute size"""

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

    def my_print(self):
        """this method prints in stdout the square with the character #"""

        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()
