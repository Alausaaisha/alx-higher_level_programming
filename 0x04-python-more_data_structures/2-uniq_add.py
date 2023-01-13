#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_of_integers = 0
    list_set = set(my_list)
    for i in list_set:
        sum_of_integers += i
    return(sum_of_integers)
