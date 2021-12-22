#!/usr/bin/python3
"""This module provides function `save_to_json_file`.
"""


def save_to_json_file(my_obj, filename):
    """Saves obj to jason file.
    Args:
       my_obj: A pythn obj
       filename (str): File name
    """
    import json

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
