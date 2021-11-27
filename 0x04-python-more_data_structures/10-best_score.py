#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    items = list(a_dictionary.items())
    big_key, big_val = items[0]
    for key, val in items:
        if val > big_val:
            big_key = key
            big_val = val
    return big_key
