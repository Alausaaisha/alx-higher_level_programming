#!/usr/bin/python3
"""this modules contains a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """this class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method initializes instance with stated attributes"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """this method retrieves the value of the attribute width"""

            return(self.__width)

        @width.setter
        def width(self, value):
            """this method sets the value of the attribute width"""

            self.__width = value

        @property
        def height(self):
            """this method retrieves the value of the attribute height"""

            return(self.__height)

        @height.setter
        def height(self, value):
            """this method sets the value of the attribute height"""

            self.__height = value

        @property
        def x(self):
            """this method retrieves the value of the attribute x"""

            return(self.__x)

        @x.setter
        def x(self, value):
            """this method sets the value of the attribute x"""

            self.__x = value

        @property
        def y(self):
            """this method retrieves the value of the attribute x"""

            return(self.__y)

        @y.setter
        def y(self, value):
            """this method sets the value of the attribute y"""

            self.__y = value
