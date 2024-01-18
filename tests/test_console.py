#!/usr/bin/python3
""" Module doc"""
import unittest
import console


class test_Console(unittest.TestCase):
    """doc"""

    def test_documentation(self):
        """doc"""
        self.assertIsNotNone(console.__doc__)
