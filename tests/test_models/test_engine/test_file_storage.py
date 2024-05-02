#!/usr/bin/python3
""" Module for testing file storage"""
import os
import unittest

from models import storage
from models.base_model import BaseModel


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
class TestFileStorage(unittest.TestCase):
    """ Class to test the file storage method """
    def setUp(self):
        """ Set up test environment """
        keys_to_delete = []
        for key in storage.all().keys():
            keys_to_delete.append(key)
        for key in keys_to_delete:
            del storage.all()[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_empty_object_list(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_add_new_object(self):
        """ New object is correctly added to __objects """
        new_object = BaseModel()
        new_object.save()
        for obj in storage.all().values():
            temp_object = obj
        self.assertTrue(temp_object is obj)

    def test_all_objects_returned(self):
        """ __objects is properly returned """
        new_object = BaseModel()
        temp_objects = storage.all()
        self.assertIsInstance(temp_objects, dict)

    def test_base_model_instantiation(self):
        """ File is not created on BaseModel save """
        new_object = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_data_saved_to_file(self):
        """ Data is saved to file """
        new_objects = BaseModel()
        data = new_object.to_dict()
        new_object.save()
        new_object2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save_method_method(self):
        """ FileStorage save method """
        new_object = BaseModel()
        new_object.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload_method(self):
        """ Storage file is successfully loaded to __objects """
        new_object = BaseModel()
        new_object.save()
        storage.reload()
        loaded_object = None
        for obj in storage.all().values():
            loaded_object = obj
        self.assertEqual(new_object.to_dict()['id'], loaded_object.to_dict()['id'])

    def test_reload_empty_file(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent_file(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)

    def test_base_model_save_method(self):
        """ BaseModel save method calls storage save """
        new_object = BaseModel()
        new_object.save()
        self.assertTrue(os.path.exists('file.json'))

    def test__file_path_type(self):
        """ Confirm __file_path is string """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_objects_type(self):
        """ Confirm __objects is a dict """
        self.assertEqual(type(storage.all()), dict)

    def test_key_formatting(self):
        """ Key is properly formatted """
        new_object = BaseModel()
        _id = new_object.to_dict()['id']
        temp_key = ''
        new_object.save()
        for key, value in storage.all().items():
            if value is new_object:
                temp_key = key
        self.assertEqual(temp_key, 'BaseModel' + '.' + _id)

    def test_storage_object_creation(self):
        """ FileStorage object storage created """
        from models.engine.file_storage import FileStorage
        self.assertEqual(type(storage), FileStorage)
