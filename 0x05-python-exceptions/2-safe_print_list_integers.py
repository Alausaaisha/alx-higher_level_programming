#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    number_of_elements_printed = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            number_of_elements_printed += 1
        except (ValueError, TypeError):
            i += 1
    print()
    return(number_of_elements_printed)
