#!/usr/bin/python3
"""document document"""

from models.engine.db_storage import DBStorage
import os
import unittest


@unittest.skipIf(
    os.getenv("HBNB_TYPE_STORAGE") != "db",
    "Test not applicabe for DBStorage"
)
class test_DB_Storage(unittest.TestCase):
    """doc"""

    def test_documentation(self):
        """doc"""
        self.assertIsNot(DBStorage.__doc__, None)
