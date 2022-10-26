#!/usr/bin/python3
"""Module test_base_model

This Module contains a tests for Base Class
"""

import inspect
import unittest

import pycodestyle
from models import base_model

Base = base_model.Base


class TestBaseDocsAndStyle(unittest.TestCase):
    """Tests Base class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            ["models/base_model.py", "tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(base_model.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(Base, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(Base.__name__, "Base")


class TestBase(unittest.TestCase):
    """Test cases for Base Class"""
    pass
