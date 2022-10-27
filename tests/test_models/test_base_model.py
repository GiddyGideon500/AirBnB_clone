#!/usr/bin/python3
"""Module test_base_model

This Module contains a tests for Base Class
"""

import inspect
import unittest
from uuid import UUID

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

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes - "id" "create_at" and
        "updated_at" exist."""
        temp = Base()
        req_att = ["id", "created_at", "updated_at"]
        for attrib in req_att:
            self.assertTrue(hasattr(temp, attrib))

    def test_id_attribute_shall_be_uuid4(self):
        """tests wether id attribute is of type string representation of
        datetime"""
        temp = Base()

        self.assertTrue(isinstance(temp.id, str))

        try:
            _ = UUID(temp.id, version=4)
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)
