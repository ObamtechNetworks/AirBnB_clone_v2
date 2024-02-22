#!/usr/bin/python3
""" test cases for the place class"""
import json
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class test_Place(test_basemodel):
    """ unittest for the place model"""

    def __init__(self, *args, **kwargs):
        """ initizalization """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city id in place class"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ tests user id """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ test place name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ test description """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ test number of rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ test number of bathrooms"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ test max guest value"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ test price by night value"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ tests place latitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ test place's longitude"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ tests place's amenity_ids"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

class test_create_place(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.storage = FileStorage()
        cls.storage.reload()

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_create_place(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_str = "Place.{}".format(output.getvalue().strip())
            self.assertIn(test_str, self.storage.all().keys())
