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


class TestHBNBCommand(unittest.TestCase):

    def test_prompt(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)