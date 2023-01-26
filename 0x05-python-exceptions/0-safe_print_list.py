#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    num_of_elements_printed = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
            num_of_elements_printed += 1
        except IndexError:
            break
    print()
    return(num_of_elements_printed)
