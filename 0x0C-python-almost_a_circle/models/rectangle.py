#!/usr/bin/python3
"""this modules contains a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """this class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method initializes instance with stated attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """this method retrieves the value of the attribute width"""

        return(self.__width)

    @width.setter
    def width(self, value):
        """this method sets the value of the attribute width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """this method retrieves the value of the attribute height"""

        return(self.__height)

    @height.setter
    def height(self, value):
        """this method sets the value of the attribute height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """this method retrieves the value of the attribute x"""

        return(self.__x)

    @x.setter
    def x(self, value):
        """this method sets the value of the attribute x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """this method retrieves the value of the attribute x"""

        return(self.__y)

    @y.setter
    def y(self, value):
        """this method sets the value of the attribute y"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area value of the
        Rectangle instance"""

        return(self.width * self.height)

    def display(self):
        """this methods prints in the stdout the Rectangle instance
        with the character #"""

        if self.y > 0:
            print('\n' * self.y, end='')
        for i in range(self.height):
            if self.x > 0:
                print(' ' * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """this method overrides the inbuilt __str__"""

        return("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height))

    def update(self, *args, **kwargs):
        """this method assigns an argument to each attribute"""

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs['id']
                elif key == 'width':
                    self.__width = kwargs['width']
                elif key == 'height':
                    self.__height = kwargs['height']
                elif key == 'x':
                    self.__x = kwargs['x']
                elif key == 'y':
                    self.__y = kwargs['y']

    def to_dictionary(self):
        """this method returns the dictionary representation of a Rectangle"""

        return({'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y})
