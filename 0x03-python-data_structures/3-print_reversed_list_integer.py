#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    if len(my_list) < 1:
        return my_list
    for i in range(-1, -(1 + len(my_list)), -1):
        print('{:d}'.format(my_list[i]))
