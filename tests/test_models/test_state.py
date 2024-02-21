#!/usr/bin/python3
""" test cases for the state classs"""
import json
import os
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class test_state(test_basemodel):
    """ unittests cases for the state class"""
    def __init__(self, *args, **kwargs):
        """ initialization """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State
    def test_name3(self):
        """ test state name """
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
    def test_create_state(self):
        hbnb_command = HBNBCommand()
        file_storage = FileStorage()
        command = "State name='California'"
        hbnb_command.do_create(command)
        #check states
        file_storage.reload()
        total_states = file_storage.all(State)
        self.assertNotEqual(total_states, {}, "No State objects found in storage after do_create function.")
        self.assertEqual(len(total_states), 1, "Incorrect number of states in the new State object.")
        #check details of created state
        new_state = next(iter(total_states.values()), None)
        self.assertIsNotNone(new_state, "New State not found in storage.")
        self.assertEqual(new_state.name.strip("'"), 'California', "Incorrect state name in the new State object.")
