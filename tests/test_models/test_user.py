#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test"""

    def setUp(self):
        """Test"""
        pass

    def tearDown(self):
        """Test"""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Test"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_to_dict(self):
        """Test"""
        us = User()
        us_dict = us.to_dict()
        self.assertEqual(str, type(us_dict["id"]))
        self.assertEqual(str, type(us_dict["created_at"]))
        self.assertEqual(str, type(us_dict["updated_at"]))

    def test_8_instantiation(self):
        """Test"""
        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_to_dict_with_argument(self):
        """Test"""
        case = User()
        with self.assertRaises(TypeError):
            case.to_dict(None)


if __name__ == "__main__":
    unittest.main()
