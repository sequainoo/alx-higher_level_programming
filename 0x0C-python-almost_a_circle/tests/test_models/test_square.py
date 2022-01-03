#!/usr/bin/python3
"""Test cases for the Square class."""
from models.rectangle import Rectangle
from models.square import Square
from contextlib import redirect_stdout
from io import StringIO
import pep8
import unittest


class TestPep8(unittest.TestCase):
    """Test pep8 compliance."""
    def test_pep8(self):
        style = pep8.StyleGuide(quite=False)
        files = ['models/square.py', 'tests/test_models/test_square.py']
        errors = style.check_files(files).total_errors
        self.assertEqual(errors, 0)


class TestInheritance(unittest.TestCase):
    """Test Square inheritance."""
    def test_inheritance(self):
        """Inheritance test."""
        self.assertTrue(issubclass(Square, Rectangle))


class TestSquareAttributes(unittest.TestCase):
    '''Test attributes of Square instance.'''
    def test_attributes(self):
        sqr = Square(6)

        self.assertEqual(sqr.width, 6)
        self.assertEqual(sqr.height, 6)
        self.assertEqual(sqr.x, 0)
        self.assertEqual(sqr.y, 0)


class TestSquareValidation(unittest.TestCase):
    '''Test input validation of square.'''
    def test_validation(self):
        '''Input validation test.'''
        with self.assertRaises(TypeError):
            sqr = Square('6')


class TestSquareStr(unittest.TestCase):
    '''Test str representation of Square.'''
    def test__str__(self):
        '''Test str(square).'''
        sqr = Square(6)
        output = str(sqr)
        expected = '[Square] ({}) {}/{} - {}'\
            .format(sqr.id, sqr.x, sqr.y, sqr.width)
        self.assertEqual(output, expected)


class TestArea(unittest.TestCase):
    '''Test area of square.'''
    def test_area(self):
        s = Square(6)
        output = s.area()
        expected = 36
        self.assertEqual(output, expected)


class TestDisplay(unittest.TestCase):
    '''Test square display() method.'''
    def test_display(self):
        '''test display'''
        s = Square(3)
        with StringIO() as buf, redirect_stdout(buf):
            s.display()
            output = buf.getvalue()
            expected = '###\n###\n###\n'
        self.assertEqual(output, expected)


class TestSizeProperty(unittest.TestCase):
    '''Test size property of square.'''
    def test_size_getter(self):
        '''Test size getter.'''
        sqr = Square(6)
        self.assertEqual(sqr.size, 6)

    def test_size_setter(self):
        '''Test size setter.

        Test width and height properties and atributes
        are set as well
        '''
        sqr = Square(6)
        sqr.size = 3
        self.assertEqual(sqr.size, 3)
        self.assertEqual(sqr.width, 3)
        self.assertEqual(sqr.height, 3)


class TestUpdate(unittest.TestCase):
    '''Test update() method of a square.'''
    def test_update(self):
        '''Tests the update() method.'''
        sqr = Square(10)

        sqr.update(89)
        self.assertEqual(sqr.id, 89)

        sqr.update(89, 2)
        self.assertEqual(sqr.size, 2)
        self.assertEqual(sqr.height, 2)
        self.assertEqual(sqr.width, 2)

        sqr.update(89, 2, 3)
        self.assertEqual(sqr.x, 3)

        sqr.update(89, 2, 3, 4)
        self.assertEqual(sqr.y, 4)

        sqr.update(89, 2, 3, 4, 5)
        self.assertEqual(
            [sqr.id, sqr.size, sqr.width, sqr.height, sqr.x, sqr.y],
            [89, 2, 2, 2, 3, 4]
            )

        sqr.update()
        self.assertEqual(
            [sqr.id, sqr.size, sqr.width, sqr.height, sqr.x, sqr.y],
            [89, 2, 2, 2, 3, 4])


class TestToDictionary(unittest.TestCase):
    '''Test to_dictionary().'''
    def test_dictionary_representation(self):
        '''Tests dictionary of square instance.'''
        s = Square(10, 2, 9, 12)
        expected = {
            'id': 12,
            'size': 10,
            'x': 2,
            'y': 9,
        }
        output = s.to_dictionary()
        self.assertEqual(output, expected)
