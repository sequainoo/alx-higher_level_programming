#!/usr/bin/python3
'''Contains tests for the base module.'''
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json
import unittest
import pep8


class TestPep8(unittest.TestCase):
    def test_pep8_style(self):
        '''Test pep8 compliance for test file and base.py.'''
        files = ['models/base.py', 'tests/test_models/test_base.py']
        style = pep8.StyleGuide(quite=False)
        errors = style.check_files(files).total_errors
        self.assertEqual(errors, 0)


class TestBase(unittest.TestCase):
    '''Test case for the Base class.'''
    def test_instantiation(self):
        '''Test creating instances.'''
        b = Base()
        b2 = Base(20)

        self.assertTrue(isinstance(b, Base))
        self.assertTrue(isinstance(b2, Base))

        with self.assertRaises(TypeError):
            b3 = Base(3, 3)
            b4 = Base(3, 3, 4)

    def test_attribute(self):
        '''Test id attribute.'''
        b = Base(20)
        self.assertEqual(b.id, 20)

    def test_to_json_string(self):
        '''Test to json string.'''
        s = Square(4, id=20)
        d = {
            'id': 20,
            'size': 4,
            'x': 0,
            'y': 0,
        }
        expected = json.dumps([d], sort_keys=True)
        output = Base.to_json_string([s.to_dictionary()])
        self.assertEqual(output, expected)

    def test_save_to_file(self):
        sqr = Square(12, id=2)
        sqr1 = Square(20, id=4)

        Square.save_to_file([sqr])
        expected = Base.to_json_string([sqr.to_dictionary()])
        with open('Square.json', mode='r', encoding='utf-8') as jf:
            output = jf.read()
            self.assertEqual(output, expected)


class TestFromJsonString(unittest.TestCase):
    def test_from_json_string(self):
        """Test JSON string translates into Python dict"""
        s0 = '[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},\
               {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}]'
        strs0 = Base.from_json_string(s0)
        self.assertTrue(type(s0) == str)
        self.assertTrue(type(strs0) == list)
        self.assertTrue(type(strs0[0]) == dict)
        self.assertTrue(strs0,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
        self.assertTrue(strs0[0],
                        {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5})

    def test_from_none_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s2 = None
        strs2 = Base.from_json_string(s2)
        self.assertTrue(type(strs2) == list)
        self.assertTrue(strs2 == [])

    def test_from_empty_json_string(self):
        """Test no JSON string translates into empty Python dict"""
        s3 = ""
        strs3 = Base.from_json_string(s3)
        self.assertTrue(type(strs3) == list)
        self.assertTrue(strs3 == [])

    # review
    def test_create(self):
        """Test transferring attribute dictionary to another instance"""
        r = Rectangle(3, 5, 1, 2, 99)
        rdic = r.to_dictionary()
        r2 = Rectangle.create(**rdic)
        self.assertEqual(str(r), '[Rectangle] (99) 1/2 - 3/5')
        self.assertEqual(str(r2), '[Rectangle] (99) 1/2 - 3/5')
        self.assertIsNot(r, r2)

    """Test saving JSON string repr of dict to class specific file"""
    # def test_save_to_file(self):
    #     """Test save to file"""
    #     r = Rectangle(10, 7, 2, 8, 99)
    #     r2 = Rectangle(2, 4, 2, 2, 98)
    #     Rectangle.save_to_file([r, r2])
    #     with open("Rectangle.json", "r") as file:
    #         self.assertEqual(
    #             json.dumps([r.to_dictionary(), r2.to_dictionary()]),
    #             file.read())

    # def test_save_none_to_file(self):
    #     """Test save None to file"""
    #     Rectangle.save_to_file(None)
    #     with open("Rectangle.json", "r") as file:
    #         self.assertEqual('[]', file.read())

    # def test_empty_none_to_file(self):
    #     """Test save empty list to file"""
    #     Rectangle.save_to_file([])
    #     with open("Rectangle.json", "r") as file:
    #         self.assertEqual('[]', file.read())

    """Test loading list of instances from JSON string repr of dict in file"""
    def test_load_from_file(self):
        """Test load from file"""
        r = Rectangle(10, 7, 2, 8, 99)
        r2 = Rectangle(2, 4, 2, 2, 98)
        Rectangle.save_to_file([r, r2])
        recs = Rectangle.load_from_file()
        self.assertEqual(len(recs), 2)
        for k, v in enumerate(recs):
            if k == 0:
                self.assertEqual(str(v), '[Rectangle] (99) 2/8 - 10/7')
            if k == 1:
                self.assertEqual(str(v), '[Rectangle] (98) 2/2 - 2/4')

    # def test_load_from_none_file(self):
    #     """Test load from None file"""
    #     Rectangle.save_to_file(None)
    #     recs = Rectangle.load_from_file()
    #     self.assertEqual(type(recs), list)
    #     self.assertEqual(len(recs), 0)

    # def test_load_from_empty_file(self):
    #     """Test load from empty file"""
    #     Rectangle.save_to_file([])
    #     recs = Rectangle.load_from_file()
    #     self.assertEqual(type(recs), list)
    #     self.assertEqual(len(recs), 0)
