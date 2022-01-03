#!/usr/bin/python3
"""This module contains the base of the models."""
import json


class Base(object):
    """The base class of all models.

    Args:
        id: The id.

    Attributes:
        id: The identity of the instance
        __nb_objects: class attr represents number of objects
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries, sort_keys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save object to json file.

        File name is classname.json
        '''
        if list_objs:
            l = [obj.to_dictionary() for obj in list_objs]
            s = Base.to_json_string(l)
            filename = '{}.json'.format(cls.__name__)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(s)
