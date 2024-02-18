#!/usr/bin/python3
""" module to test city class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


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
