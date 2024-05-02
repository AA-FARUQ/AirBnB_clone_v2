#!/usr/bin/python3
"""Unit tests module for Amenity model. """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenityModel(TestBasemodel):
    """Represents the unit tests for the Amenity model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = "Amenity"
        self.model_cls = Amenity

    def test_name_type(self):
        """Checks the type of 'name' attribute."""
        new_instance = self.model_cls()
        self.assertEqual(
            type(new_instance.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
