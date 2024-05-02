#!/usr/bin/python3
"""Unit tests module for City model."""
import os

from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestCityModel(TestBaseModel):
    """Represents the unit tests for the City model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = "City"
        self.model_class = City

    def test_state_id(self):
        """Tests the type of state_id."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.state_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name_type(self):
        """Tests the type of name."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
