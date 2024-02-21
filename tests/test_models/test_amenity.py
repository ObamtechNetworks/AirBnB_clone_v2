#!/usr/bin/python3
""" module to test amenity class"""
import json
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class test_Amenity(test_basemodel):
    """ test amenity class"""

    def __init__(self, *args, **kwargs):
        """ instance initialization """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ test amenity name"""
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

            def test_create_amenity(self):
                hbnb_command = HBNBCommand()
                file_storage = FileStorage()
                command = "Amenity name='Swimming_Pool'"
                hbnb_command.do_create(command)
                #check states
                file_storage.reload()
                total_amenities = file_storage.all(Amenity)
                self.assertNotEqual(total_amenities, {}, "No Amenity objects found in storage after do_create function.")
                self.assertEqual(len(total_amenities), 1, "Incorrect number of amenities in the new Amenity object.")
                #check details of created amenities
                new_amenities = next(iter(total_amenities.values()), None)
                self.assertIsNotNone(new_amenities, "New Amenity not found in storage.")
                self.assertEqual(new_state.name.strip("'"), 'Swimming Pool', "Incorrect state name in the new State object.")
