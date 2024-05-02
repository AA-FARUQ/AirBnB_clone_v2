#!/usr/bin/python3
"""Unit tests module for User model."""
import os
from sqlalchemy import Column

from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUserModel(TestBaseModel):
    """Represents the tests for the User model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = "User"
        self.model_class = User

    def test_first_name_type(self):
        """Tests the type of first_name."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.first_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_last_name_type(self):
        """Tests the type of last_name."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.last_name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_email_type(self):
        """Tests the type of email."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.email),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_password_type(self):
        """Tests the type of password."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.password),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
