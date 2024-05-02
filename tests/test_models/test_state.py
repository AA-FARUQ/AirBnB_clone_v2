#!/usr/bin/python3
"""Unit tests module for State model."""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestStateModel(TestBaseModel):
    """Represents the unit tests for the State model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.model_name = "State"
        self.model_class = State

    def test_name_type(self):
        """Tests the type of name."""
        new_instance = self.model_class()
        self.assertEqual(
            type(new_instance.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )
