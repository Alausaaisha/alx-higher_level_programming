#!/usr/bin/python3
"""this module contains a function that reads a text file (UTF8)
and prints it to stdout"""


def read_file(filename=""):
    """method that reads a text file (UTF8) and prints it to stdout:"""

    with open(filename, 'r', encoding="UTF8") as f:
        print(f.read(), end='')
