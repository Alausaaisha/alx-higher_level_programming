#!/usr/bin/python3
"""this module writes a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """method instantiates with width and height"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """this method returns the area of the rectangle"""

        return(self.__height * self.__width)

    def __str__(self):
        """this method returns and prints rectangle in presentable string
        format"""

        return("[Rectangle] {}/{}".format(self.__width, self.__height))
