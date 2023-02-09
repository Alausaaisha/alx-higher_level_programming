#!/usr/bin/python3
"""this module writes class BaseGeometry"""


class BaseGeometry:
    """class created"""

    def area(self):
        """Public instance method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validates value"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
