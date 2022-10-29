#!/usr/bin/python3
"""Module test_file_storage

This Module contains a tests for FileStorage Class
"""

import inspect
import unittest

import pycodestyle
from models.engine import file_storage

FileStorage = file_storage.FileStorage


class TestFileStorageDocsAndStyle(unittest.TestCase):
    """Tests FileStorage class for documentation and style conformance"""

    def test_pycodestyle(self):
        """Tests compliance with pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(
            [
                "models/engine/file_storage.py",
                "tests/test_models/test_engine/test_file_storage.py"
            ])
        self.assertEqual(result.total_errors, 0)

    def test_module_docstring(self):
        """Tests whether the module is documented"""
        self.assertTrue(len(file_storage.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests whether the class is documented"""
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(FileStorage, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(FileStorage.__name__, "FileStorage")


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage Class"""
    pass
