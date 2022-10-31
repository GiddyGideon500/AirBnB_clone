#!/usr/bin/python3
"""Module test_amenity

This Module contains a tests for Amenity Class
"""

import os
import unittest
from io import StringIO
from unittest.mock import patch

from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Tests the console app"""
    @classmethod
    def setUpClass(cls) -> None:
        """sets up the test console"""
        cls.cmd = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """removes the file.json temporary file"""
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_create_prints_class_name_error(self):
        """tests the create command class name error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create')
            self.assertEqual("** class name missing **\n",
                             output.getvalue())

    def test_create_prints_class_does_not_exist(self):
        """tests the create command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BModel')
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())

    def test_create_creates_an_object(self):
        """tests the create command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue()
            self.assertNotIn(id, [None, ""])

        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd(f'show BaseModel {id}')
            self.assertIn(id.strip('\n'), output.getvalue())

    def test_show_prints_class_name_error(self):
        """tests the show command class name error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('show')
            self.assertEqual("** class name missing **\n",
                             output.getvalue())

    def test_show_prints_class_does_not_exist(self):
        """tests the show command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('show BModel')
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())

    def test_show_displays_an_object(self):
        """tests the show command class not found error"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.cmd.onecmd('create BaseModel')
            id = output.getvalue().strip('\n')
            self.cmd.onecmd(f'show BaseModel {id}')
            self.assertIn("BaseModel", output.getvalue())
