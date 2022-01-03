#!/usr/bin/python3
"""Implements the rectangle class."""
from models.base import Base
import sys


class Rectangle(Base):
    """Rectangle implementation.

    Attributes:
        __width: width
        __height: height.
        __x: x
        __y: y
    Args:
        width: rectangles's width
        height: retcangle's height
        x: x
        y: y
        id: id of rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        # Validate width
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')

        # Validate height
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')

        # Validate x
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')

        # Validate y
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for the width attribute"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of the rectangle."""
        # Validate width
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Getter for the height attribute"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of the rectangle."""
        # Validate height
        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x attribute."""
        # Validate x
        if type(x) is not int:
            raise TypeError('x must be an integer')
        if x <= 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the y attribute."""
        # Validate width
        if type(y) is not int:
            raise TypeError('y must be an integer')
        if y <= 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """computes area of rectangle."""
        return self.width * self.height

    def display(self):
        """Displays rectangle.

        Example:
            Rectangle(3, 4).display()
            ###
            ###
            ###
            ###
        """
        if self.y:
            for x in range(self.y):
                sys.stdout.write('\n')
        for i in range(self.height):
            if self.x:
                for x in range(self.x):
                    sys.stdout.write(' ')
            for j in range(self.width):
                sys.stdout.write('#')
            sys.stdout.write('\n')

    def __str__(self):
        """..."""
        name = self.__class__.__name__
        return '[{}] ({}) {}/{} - {}/{}'\
            .format(name, self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates rectangle's attributes.

        Args:
            *args: (id, width, height, x, y)
        """
        if args and len(args) > 0:
            if len(args) == 5:
                self.id, self.width, self.height, self.x, self.y = args
            if len(args) == 4:
                self.id, self.width, self.height, self.x = args
            if len(args) == 3:
                self.id, self.width, self.height = args
            if len(args) == 2:
                self.id, self.width = args
            if len(args) == 1:
                self.id, = args
        elif kwargs:
            items = kwargs.items()
            for key, value in items:
                # r_dict[key] = value
                if key == 'height':
                    self.height = value
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''Returns the dict representation of the object.'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
            }
