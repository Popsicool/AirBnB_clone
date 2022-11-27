#!/usr/bin/python3
"""
Test module for console.py

"""


import unittest
import os
import sys
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """Test class for console"""

    def test_prompt(self):
        """Test prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_help_quit(self):
        """test help quit"""
        a = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(a, output.getvalue().strip())

    def test_help_EOF(self):
        """Test help EOF"""
        a = "handles the end of file"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(a, output.getvalue().strip())

    def test_help_show(self):
        """Test help show"""
        a = "Prints the string representation"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(a, output.getvalue().strip())

    def test_help_create(self):
        """Test help create"""
        a = "Creates a new instance of BaseModel"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(a, output.getvalue().strip())

    def test_help_destroy(self):
        """Test help destroy"""
        a = "Deletes an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(a, output.getvalue().strip())

    def test_help_update(self):
        """Test help update"""
        a = "Updates an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(a, output.getvalue().strip())

    def test_help_all(self):
        """test help all"""
        a = "Prints all string representation"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(a, output.getvalue().strip())

    @classmethod
    def setUp(self):
        """set up for testing"""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    @classmethod
    def tearDown(self):
        """Tear down after testing"""
        if os.path.isfile("file.json"):
            os.remove("file.json")

    def test_quit(self):
        """Test quit"""
        with patch("sys.stdout", new=StringIO()) as result:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """test EOF"""
        with patch("sys.stdout", new=StringIO()) as result:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_create_with_no_class_name(self):
        """test create with no class name"""
        result = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(result, output.getvalue().strip())

    def test_create_with_invalid_className(self):
        """test create with invalid classname"""
        result = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create XYD"))
            self.assertEqual(result, output.getvalue().strip())

    def test_invalid_syntax(self):
        """test inalid syntax"""
        result = "*** Unknown syntax: All"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("All"))
            self.assertEqual(result, output.getvalue().strip())
