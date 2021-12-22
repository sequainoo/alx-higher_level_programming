#!/usr/bin/python3
'''Provides a student class.
'''


class Student(object):
    '''Defines a student.
    '''
    def __init__(self, first_name, last_name, age):
        '''Initialises public attr.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        '''Gets the dictionary repr of the instance.
        '''
        return self.__dict__
