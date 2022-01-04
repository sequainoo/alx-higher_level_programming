#!/usr/bin/python3
"""Test for Rectangle class."""


from models.rectangle import Rectangle
from models.base import Base
from contextlib import redirect_stdout
from io import StringIO
import unittest
import pep8


class TestPep8(unittest.TestCase):
    """Test pep8 compliance for the rectangle module."""
    def test_pep8(self):
        """pep8 test."""
        style = pep8.StyleGuide(quite=False)
        errors = 0
        files = ['models/rectangle.py', 'tests/test_models/test_rectangle.py']
        errors = style.check_files(files).total_errors
        self.assertEqual(errors, 0, 'fix pep8')


class TestRectangle(unittest.TestCase):
    """Rectangle test."""

    def test_inheritance(self):
        """Check Rectangle inherits Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_attributes(self):
        """Test that attributes are assigned to objects as expected."""
        r = Rectangle(4, 6, 1, 1, 10)
        r1 = Rectangle(4, 3, id=4)
        r2 = Rectangle(4, 3, id=5)

        # r verifications
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 10)

        # r1 verifications
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 4)

        # r2 verify id once again
        self.assertEqual(r2.id, 5)

    def test_init_method_validations(self):
        """Validate all attributes id excluded."""
        with self.assertRaises(TypeError):
            r = Rectangle('1', '0', '0')

        with self.assertRaises(TypeError):
            r = Rectangle('', 3, 3, 3)
            r = Rectangle(3, '5', 5, 4)
            r = Rectangle(3, 5, '5', 4)
            r = Rectangle(3, 5, 5, '4')

        with self.assertRaises(ValueError):
            r = Rectangle(0, 2, 3, 4, None)  # width is 0
            r = Rectangle(-1, 2, 3, 4, None)  # width is under 0
            r = Rectangle(2, 0, 3, 4, None)  # height is 0
            r = Rectangle(2, -2, 1, 4, None)  # height under 0
            r = Rectangle(2, -2, -3, 4, None)  # x under 0
            r = Rectangle(0, 2, 3, -4, None)  # y under 0

    def test_setters_validations(self):
        """Test setter methods validations."""
        r = Rectangle(4, 5, 5, 6, None)
        with self.assertRaises(TypeError):
            r.width = ''
            r.width = []
            r.height = ''
            r.height = {}
            r.x = '43'
            r.x = None
            r.y = 'hey'
            r.y = (1, )

        with self.assertRaises(ValueError):
            r.width = 0
            r.width = -1
            r.height = 0
            r.height = -1
            r.x = -1
            r.y = -5

    def test_area(self):
        """Test area of the rectangle."""
        r = Rectangle(3, 4)
        r1 = Rectangle(2, 10)
        r2 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r.area(), 12)
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 56)

        with self.assertRaises(TypeError):
            r.area(89)

    def test_display(self):
        r = Rectangle(4, 6)
        r2 = Rectangle(2, 3, 2, 2)

        with StringIO() as buf, redirect_stdout(buf):
            r.display()
            s = buf.getvalue()
        self.assertEqual(s, '####\n####\n####\n####\n####\n####\n')

        with StringIO() as buf, redirect_stdout(buf):
            r2.display()
            output = buf.getvalue()
            expected = '\n\n  ##\n  ##\n  ##\n'
        self.assertEqual(output, expected)

    def test__str__(self):
        r = Rectangle(4, 3)
        actual = str(r)
        expected = '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(r.id, r.x, r.y, r.width, r.height)
        self.assertEqual(actual, expected)

    def test_update(self):
        '''Tests the update method.'''
        r = Rectangle(10, 10, 10, 10)
        r2 = Rectangle(5, 6)

        r.update(89)
        self.assertEqual(r.id, 89)

        r.update(89, 2)
        self.assertEqual(r.width, 2)

        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

        r.update(89, 2, 3)
        self.assertEqual(r.height, 3)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.x, 4)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [89, 2, 3, 4, 5])

        r.update(89, 2, 3, 4, 5, 6)
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [89, 2, 3, 4, 5])

        r.update()
        self.assertEqual([r.id, r.width, r.height, r.x, r.y], [89, 2, 3, 4, 5])

        r2.update(height=1)
        self.assertEqual(r2.height, 1)

        r2.update(width=1, x=2)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.x, 2)

        r2.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r2.x, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.y, 3)
        self.assertEqual(r2.width, 4)

        r2.update(89, id=20)
        self.assertEqual(r2.id, 89)

        r2.update(89, 7, height=13, x=3)
        self.assertEqual(r2.width, 7)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 1)


class TestToDictionary(unittest.TestCase):
    '''Test to_dictionary().'''
    def test_dictionary_representation(self):
        '''Tests dictionary of object.'''
        r = Rectangle(10, 2, 1, 9, 11)
        expected = {
            'id': 11,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 9,
        }
        output = r.to_dictionary()
        self.assertEqual(output, expected)
