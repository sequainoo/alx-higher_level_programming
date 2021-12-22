#!/usr/bin/python3
'''Contains function that gives JSON representation of an object.
'''


def to_json_string(my_obj):
    '''Gives json repr of an object

    Args:
        my_obj: python object
    Return:
        JSON string of the object
    '''
    import json
    
    return json.dumps(my_obj)
