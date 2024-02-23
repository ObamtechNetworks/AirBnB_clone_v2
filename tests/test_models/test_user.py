#!/usr/bin/python3
""" test cases for the user model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import json
import os
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO


class test_User(test_basemodel):
    """ test cases for the user model, unittests"""

    def __init__(self, *args, **kwargs):
        """ initialization"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ tests first name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """ tests user last name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ tests user email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ tests user password"""
        new = self.value()
        self.assertEqual(type(new.password), str)

class test_create_user(unittest.TestCase):
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

    def test_create_user(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_str = "User.{}".format(output.getvalue().strip())
            self.assertIn(test_str, self.storage.all().keys())
