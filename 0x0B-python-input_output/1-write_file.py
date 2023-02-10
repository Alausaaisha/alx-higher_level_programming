#!/usr/bin/python3
"""this module contains a function that writes a string to a text file
(UTF8) and returns the number of characters written"""


def write_file(filename="", text=""):
    """this method writes a string to a text file (UTF8) and
    returns the number of characters written"""

    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)
        return(len(text))
