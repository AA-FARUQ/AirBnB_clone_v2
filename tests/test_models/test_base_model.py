#!/usr/bin/python3
"""Unit tests module for BaseModel. """
from datetime import datetime
import json
import os
import unittest
from uuid import UUID

from models.base_model import BaseModel, Base


class TestBasemodel(unittest.TestCase):
    """Represents the tests for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = 'BaseModel'
        self.model_class = BaseModel

    def setUp(self):
        """Performs some operations before the tests are run."""
        pass

    def tearDown(self):
        """Performs some operations after the tests are run"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """Tests the initialization of the model class."""
        self.assertIsInstance(self.model_class(), BaseModel)
        if self.model_class is not BaseModel:
            self.assertIsInstance(self.model_class(), Base)
        else:
            self.assertNotIsInstance(self.model_class(), Base)

    def test_default(self):
        """Tests the type of value stored."""
        instance = self.model_class()
        self.assertEqual(type(instance), self.model_class)

    def test_kwargs(self):
        """Tests kwargs with an int."""
        instance = self.model_class()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        """Tests kwargs with an int."""
        instance = self.model_class()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new_instance = BaseModel(**copy)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_save(self):
        """Tests the save function of the BaseModel class."""
        instance = self.model_class()
        instance.save()
        key = self.model_name + "." + instance.id
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str(self):
        """Tests the __str__ function of the BaseModel class."""
        instance = self.model_class()
        self.assertEqual(str(instance), '[{}] ({}) {}'.format(self.model_name, instance.id,
                         instance.__dict__))

    def test_todict(self):
        """Tests the to_dict function of the model class."""
        instance = self.model_class()
        n = instance.to_dict()
        self.assertEqual(instance.to_dict(), n)
        # Tests if it's a dictionary
        self.assertIsInstance(self.model_class().to_dict(), dict)
        # Tests if to_dict contains accurate keys
        self.assertIn('id', self.model_class().to_dict())
        self.assertIn('created_at', self.model_class().to_dict())
        self.assertIn('updated_at', self.model_class().to_dict())
        # Tests if to_dict contains added attributes
        model_instance = self.model_class()
        model_instance.firstname = 'Faruq'
        model_instance.lastname = 'Akande'
        self.assertIn('firstname', model_instance.to_dict())
        self.assertIn('lastname', model_instance.to_dict())
        self.assertIn('firstname', self.model_class(firstname='Faruq').to_dict())
        self.assertIn('lastname', self.model_class(lastname='Akande').to_dict())
        # Tests to_dict datetime attributes if they are strings
        self.assertIsInstance(self.model_class().to_dict()['created_at'], str)
        self.assertIsInstance(self.model_class().to_dict()['updated_at'], str)
        # Tests to_dict output
        datetime_now = datetime.today()
        model_instance = self.model_class()
        model_instance.id = '012345'
        model_instance.created_at = model_instance.updated_at = datetime_now
        to_dict = {
            'id': '012345',
            '__class__': model.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(model_instance.to_dict(), to_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertDictEqual(
                self.model_class(id='u-b34', age=13).to_dict(),
                {
                    '__class__': model_instance.__class__.__name__,
                    'id': 'u-b34',
                    'age': 13
                }
            )
            self.assertDictEqual(
                self.model_class(id='u-b34', age=None).to_dict(),
                {
                    '__class__': model_instance.__class__.__name__,
                    'id': 'u-b34',
                    'age': None
                }
            )
        # Tests to_dict output contradiction
        model_instance_d = self.model_class()
        self.assertIn('__class__', self.model_class().to_dict())
        self.assertNotIn('__class__', self.model_class().__dict__)
        self.assertNotEqual(mdl_d.to_dict(), model_instance_d.__dict__)
        self.assertNotEqual(
            model_instance_d.to_dict()['__class__'],
            model_instance_d.__class__
        )
        # Tests to_dict with arg
        with self.assertRaises(TypeError):
            self.model_class().to_dict(None)
        with self.assertRaises(TypeError):
            self.model_class().to_dict(self.model_class())
        with self.assertRaises(TypeError):
            self.model_class().to_dict(45)
        self.assertNotIn('_sa_instance_state', n)

    def test_kwargs_none(self):
        """Tests kwargs that is empty."""
        n = {None: None}
        with self.assertRaises(TypeError):
            new_instance = self.model_class(**n)

    def test_kwargs_one(self):
        """Tests kwargs with one key-value pair."""
        n = {'Name': 'test'}
        new_instance = self.model_class(**n)
        self.assertTrue(hasattr(new_instance, 'Name'))

    def test_id(self):
        """Tests the type of id."""
        new_instance = self.model_class()
        self.assertEqual(type(new_instance.id), str)

    def test_created_at(self):
        """Tests the type of created_at."""
        new_instance = self.model_class()
        self.assertEqual(type(new_instance.created_at), datetime)

    def test_updated_at(self):
        """Tests the type of updated_at."""
        new_instance = self.model_class()
        self.assertEqual(type(new.updated_at), datetime)
        n = new_instance.to_dict()
        new_instance = BaseModel(**n)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)

    @unittest.skipIf(
        os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_delete(self):
        """Tests the delete function of the BaseModel class."""
        from models import storage
        instance = self.model_class()
        instance.save()
        self.assertTrue(i in storage.all().values())
        instance.delete()
        self.assertFalse(instance in storage.all().values())
