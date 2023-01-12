#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if type(my_list) == list:
        last_item = len(my_list) - 1
        for i in range(last_item, -1, -1):
            print('{:d}'.format(my_list[i]))
