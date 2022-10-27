#!/usr/bin/python3
"""Module test_base_model

This Module contains a tests for Base Class
"""

import inspect
import sys
import unittest
from datetime import datetime
from io import StringIO
from uuid import UUID

import pycodestyle
from models import base_model

BaseModel = base_model.BaseModel


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
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_methods_docstring(self):
        """Tests whether the class methods are documented"""
        funcs = inspect.getmembers(BaseModel, inspect.isfunction)
        for func in funcs:
            self.assertTrue(len(func.__doc__) >= 1)

    def test_class_name(self):
        """Test whether the class name is correct"""
        self.assertEqual(BaseModel.__name__, "BaseModel")


class TestBase(unittest.TestCase):
    """Test cases for Base Class"""

    def test_public_attributes_exist(self):
        """tests wether the public instance attributes - "id" "create_at" and
        "updated_at" exist."""
        temp = BaseModel()
        req_att = ["id", "created_at", "updated_at"]
        for attrib in req_att:
            self.assertTrue(hasattr(temp, attrib))

    def test_id_attribute_shall_be_uuid4(self):
        """tests wether id attribute is of type string representation of
        datetime"""
        temp = BaseModel()

        self.assertIsInstance(temp.id, str)

        try:
            _ = UUID(temp.id, version=4)
        except Exception:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    def test_datetime_attributes(self):
        """tests if created_at and updated_at instance attributes are of
        datetime type"""
        temp = BaseModel()
        self.assertIsInstance(temp.created_at, datetime)
        self.assertIsInstance(temp.updated_at, datetime)

    def test_bas_str_should_print_formatted_output(self):
        """__str__ should print [<class name>] (<self.id>) <self.__dict__>"""
        temp = BaseModel()
        temp.my_number = 89
        expected = f"[{BaseModel.__name__}] ({temp.id}) {temp.__dict__}"
        output = StringIO()
        sys.stdout = output
        print(temp)
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue().strip("\n"), expected)

    def test_public_method_attributes_exist(self):
        """tests wether public instance methods - "save" "to_dict" exist."""
        temp = BaseModel()
        req_att = ["save", "to_dict"]
        for attrib in req_att:
            self.assertTrue(hasattr(temp, attrib)
                            and callable(getattr(temp, attrib)))

    def test_save_method_updates_updated_at_value(self):
        """save method shall update updated_at"""
        temp = BaseModel()
        old_date = temp.updated_at
        temp.save()
        self.assertIsInstance(old_date, datetime)
        self.assertNotEqual(temp.updated_at, old_date)

    def test_to_dict_returns_a_dictionary_of_attributes(self):
        """to_dict should return a dictionary containing all key/value of
        self.__dict__
        """
        temp = BaseModel()
        temp_dict = temp.to_dict()
        self.assertIsInstance(temp_dict, dict)
        keys = temp_dict.keys()

        for k, v in temp.__dict__.items():
            self.assertIn(k, keys)
            if not isinstance(temp.__dict__[k], datetime):
                self.assertEqual(temp_dict[k], v)

    def test_to_dict_has_a_key_with_the_class_name(self):
        """to_dict must have a key of __class__ with a value of the classes
        name
        """
        temp = BaseModel()
        temp_dict = temp.to_dict()
        self.assertIn("__class__", temp_dict.keys())
        self.assertEqual(temp_dict["__class__"],
                         BaseModel.__name__)

    def test_to_dict_formats_dates_with_isoformat(self):
        """to_dict should store dates in isoformat"""
        temp = BaseModel()
        temp_dict = temp.to_dict()

        for k, v in temp.__dict__.items():
            if isinstance(temp.__dict__[k], datetime):
                self.assertEqual(datetime.fromisoformat(temp_dict[k]), v)

    def test_init_with_kwargs(self):
        """test that BaseClass can be constructed from kwargs"""
        temp_obj_1 = BaseModel()
        temp_obj_2 = BaseModel(**temp_obj_1.to_dict())

        for k, v in temp_obj_1.__dict__.items():
            self.assertEqual(v, temp_obj_2.__dict__[k])
