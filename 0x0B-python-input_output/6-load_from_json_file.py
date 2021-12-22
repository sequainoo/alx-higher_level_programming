#!/usr/bin/python3
"""This module provides function `load_from_json_file`.
"""


def load_from_json_file(filename):
    """Load obj from json file.
    Args:
       filename (str): File name
    """
    import json

    with open(filename, mode='r', encoding='utf-8') as f:
        json.load(f)
