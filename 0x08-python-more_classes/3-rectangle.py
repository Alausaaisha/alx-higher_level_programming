#!/usr/bin/python3
"""this module defines a class Rectangle by private instance
attributes width and height"""


class Rectangle:
    """class Rectangle created"""

    def __init__(self, width=0, height=0):
        """this method instantiates an object of the class"""

        self.width = width
        self.height = height

    def __str__(self):
        """this method prints the rectangle with the characeter #"""

        rect = ''
        if self.__width == 0 or self.height == 0:
            return("")
        else:
            for i in range(self.height):
                for j in range(self.width):
                    rect += '#'
                rect += '\n'
            return(rect)

    @property
    def width(self):
        """this method retrieves the value of the private instance
        attribute width"""

        return(self.__width)

    @width.setter
    def width(self, value):
        """this method sets the value of the attribute width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """this method retrieves the value of the private
        instance attribute height"""

        return(self.__height)

    @height.setter
    def height(self, value):
        """this method sets the value of the attribute height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """this method returns the rectangle area"""

        rectangle_area = self.width * self.height
        return(rectangle_area)

    def perimeter(self):
        """this method returns the rectangle perimeter"""

        if self.width == 0 or self.height == 0:
            rect_perimeter = 0
        else:
            rect_perimeter = 2 * (self.height + self.width)
        return(rect_perimeter)
