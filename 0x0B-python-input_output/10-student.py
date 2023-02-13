#!/usr/bin/python3
"""this module contains a class Student that defines a student
by public instances first_name, last_name, age"""


class Student:
    """class created"""

    def __init__(self, first_name, last_name, age):
        """this method is called when class is instantiated and it
        initializes with first_name, last_name, age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """this method retrieves a dictionary representation of a
        Student instance"""

        new_dict = {}

        if type(attrs) is list:
            for i in attrs:
                for key, value in self.__dict__.items():
                    if i == key:
                        new_dict[key] = value
            return(new_dict)
        return(self.__dict__)
