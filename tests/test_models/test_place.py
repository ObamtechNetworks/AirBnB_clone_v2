#!/usr/bin/python3
""" test cases for the place class"""
import json
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models.engine.file_storage import FileStorage
from console import HBNBCommand


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
    def setUp(self):
        self.file_storage = FileStorage()
        self.file_path = 'test_file.json'
        FileStorage._FileStorage__file_path = self.file_path
        self.file_storage.reload()

    def tearDown(self):
        FileStorage._FileStorage__file_path = 'file.json'
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            os.remove(self.file_path)
        except FileNotFoundError:
            pass
    
    def test_create_place(self):
        hbnb_command = HBNBCommand()
        file_storage = FileStorage()
        command = "Place name='My_little_house'"
        new_place = hbnb_command.do_create(command)

        #check place
        file_storage.reload()
        #total_places = file_storage.all(Place)
        #self.assertNotEqual(total_places, {}, "No Place objects found in storage after do_create function.")
        #self.assertEqual(len(total_places), 1, "Incorrect number of places in the new Place object.")

        #check details of created place
        #new_place = next(iter(total_places.values()), None)
        self.assertIsNotNone(new_place, "New Place not found in storage.")
        self.assertEqual(new_place.name.strip("'"), 'My little house', "Incorrect place name in the new Place object.")
