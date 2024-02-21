#!/usr/bin/python3
""" module to test city class """
import json
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class test_City(test_basemodel):
    """ test_city class"""

    def __init__(self, *args, **kwargs):
        """ instance initialization """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ test city state id"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ test city name"""
        new = self.value()
        self.assertEqual(type(new.name), str)

class test_create_state(unittest.TestCase):
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

        def test_create_city(self):
            hbnb_command = HBNBCommand()
            file_storage = FileStorage()
            command = "City name='Nairobi'"
            hbnb_command.do_create(command)
            #check states
            file_storage.reload()
            total_cities = file_storage.all(City)
            self.assertNotEqual(total_cities, {}, "No City objects found in storage after do_create function.")
            self.assertEqual(len(total_cities), 1, "Incorrect number of cities in the new City object.")
            #check details of created amenities
            new_city = next(iter(total_cities.values()), None)
            self.assertIsNotNone(new_city, "New City not found in storage.")
            self.assertEqual(new_city.name.strip("'"), 'Nairobi', "Incorrect city name in the new City object.")

        def test_create_cityid(self):
            hbnb_command = HBNBCommand()
            file_storage = FileStorage()
            command = "City state_id='0001'"
            hbnb_command.do_create(command)
            new_city = next(iter(total_cities.values()), None)
            self.assertIsNotNone(new_city, "New City not found in storage.")
            self.assertEqual(new_city.state_id.strip("'"), '0001', "Incorrect city IDin the new City object.")

