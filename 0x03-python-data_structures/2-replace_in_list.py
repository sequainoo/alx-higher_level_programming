#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # check if index is alright
    if idx >= len(my_list) or idx < 0:
        return my_list
    
    my_list[idx] = element
    return my_list
