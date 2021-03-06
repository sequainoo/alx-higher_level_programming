#!/usr/bin/python3
'''Peak finding funtion.'''


def find_peak(list_of_integers):
    '''finds one of the peaks of the list.
    element is peak if its greater than its neighbors
    '''
    length = len(list_of_integers)
    mid_index = length//2

    if not list_of_integers:
        return None
    if length == 1:
        return list_of_integers[0]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]

    left_item = list_of_integers[mid_index - 1]
    middle_item = list_of_integers[mid_index]
    if mid_index + 1 == length:
        right_item = None
    else:
        right_item = list_of_integers[mid_index + 1]

    if left_item < middle_item and\
            (not right_item or right_item < middle_item):
        return middle_item
    if left_item >= middle_item:
        list_of_integers = list_of_integers[:mid_index]
        return find_peak(list_of_integers)
    if right_item >= middle_item:
        list_of_integers = list_of_integers[mid_index + 1:]
        return find_peak(list_of_integers)
