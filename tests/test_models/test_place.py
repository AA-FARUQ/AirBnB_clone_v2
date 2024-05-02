#!/usr/bin/python3
"""Unit tests module for place model."""
import os

from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlaceModel(TestBaseModel):
    """Represents the tests for the Place model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = "Place"
        self.model_class = Place

    def test_city_id_type(self):
        """Tests the type of city_id."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id_type(self):
        """Tests the type of user_id."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name_type(self):
        """Tests the type of name."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description_type(self):
        """Tests the type of description."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms_type(self):
        """Tests the type of number_rooms."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms_type(self):
        """Tests the type of number_bathrooms."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_max_guest_type(self):
        """Tests the type of max_guest."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_price_by_night_type(self):
        """Tests the type of price_by_night."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_latitude_type(self):
        """Tests the type of latitude."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_longitude_type(self):
        """Tests the type of longitude."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.longitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids_type(self):
        """Tests the type of amenity_ids."""
        new_instance = self.model_class()
        self.assertEqual(type(new_instance.amenity_ids), list)
