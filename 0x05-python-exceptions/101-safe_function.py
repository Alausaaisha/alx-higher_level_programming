#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        func = fct(*args)
        return(func)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
