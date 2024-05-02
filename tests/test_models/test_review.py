#!/usr/bin/python3
"""Unit tests module for Review model"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReviewModel(TestBaseModel):
    """Represents the unit tests for the Review model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = "Review"
        self.model_class = Review

    def test_place_id_type(self):
        """Tests the type of place_id."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id_type(self):
        """Tests the type of user_id."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_text_type(self):
        """Tests the type of text."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
