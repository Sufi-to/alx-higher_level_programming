#!/usr/bin/python3
"""This is a unnitest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unnitest for max_integer function."""
    def test_mod_doc(self):
        doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(doc) > 1)

    def test_fun_doc(self):
        doc = __import__("6-max_integer").__doc__
        self.asserTrue(len(doc) > 1)

