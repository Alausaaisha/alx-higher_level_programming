#!/usr/bin/python3
"""this modules contains a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """this class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method initializes instance with stated attributes"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """this method retrieves the value of the attribute width"""

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
            """this method retrieves the value of the attribute height"""

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

        @property
        def x(self):
            """this method retrieves the value of the attribute x"""

            return(self.__x)

        @x.setter
        def x(self, value):
            """this method sets the value of the attribute x"""

            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

        @property
        def y(self):
            """this method retrieves the value of the attribute x"""

            return(self.__y)

        @y.setter
        def y(self, value):
            """this method sets the value of the attribute y"""

            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value
