#!/usr/bin/python3
""" test cases for the user model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


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
