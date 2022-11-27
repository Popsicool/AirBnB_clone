#!/usr/bin/python3
"""Test city """

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """test"""

    def setUp(self):
        """test"""
        pass

    def tearDown(self):
        """test"""
        pass

    def resetStorage(self):
        """test"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_25(self):
        """test"""
        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_27(self):
        """"test"""
        st = City()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_28(self):
        """"test"""
        st = City()
        st.middle_name = "Holberton"
        st.my_number = 98
        self.assertEqual("Holberton", st.middle_name)
        self.assertIn("my_number", st.to_dict())

    def test_29(self):
        """"test"""
        st = City()
        st_dict = st.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))


if __name__ == "__main__":
    unittest.main()
