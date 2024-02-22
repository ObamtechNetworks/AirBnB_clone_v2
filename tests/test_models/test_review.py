#!/usr/bin/python3
""" tests cases for the review model"""
import json
import os
import unittest
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ unittests for the review object model"""

    def __init__(self, *args, **kwargs):
        """ initialization"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ tests place id"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ tests user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ tests texts"""
        new = self.value()
        self.assertEqual(type(new.text), str)

class test_create_review(unittest.TestCase):
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

    def test_create_review(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            test_str = "Review.{}".format(output.getvalue().strip())
            self.assertIn(test_str, self.storage.all().keys())
