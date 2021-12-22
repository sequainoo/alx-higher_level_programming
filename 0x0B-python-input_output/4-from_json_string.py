#!/usr/bin/python3
'''Module provides a function that returns an object from json.
'''


def from_json_string(my_str):
    '''Makes an object from json.
    Args:
        mystr (str): json string
    Return:
        A python object
    ''''
    import json

    return (json.loads(my_str))
