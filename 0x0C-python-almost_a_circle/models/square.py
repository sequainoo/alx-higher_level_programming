#!/usr/bin/python3
"""Implements the square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square extends Rectangle.

    Attributes:
        width: width
        height:
        x:
        y:
        id:
    Args:
        size: Size of the square.
        x: x cordinate
        y: y cordinate
        id: id of the square object
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representaion of square."""
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update square.

        Args:
            *args: (id, size, x, y)
            *kwargs: (id, size, x, y)
        '''
        if args and len(args) > 0:
            if len(args) == 1:
                super().update(*args)
            arguments = []
            for i in range(len(args)):
                if i is 1:
                    arguments.append(args[i])
                    arguments.append(args[i])
                else:
                    arguments.append(args[i])
            super().update(*arguments)
        elif kwargs:
            kwarguments = {}
            for key, value in kwargs.items():
                if key == 'size':
                    kwarguments['width'] = value
                    kwarguments['height'] = value
                else:
                    kwarguments[key] = value
            super().update(**kwarguments)

    def to_dictionary(self):
        '''Returns the dict representation of the square.'''
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
            }
