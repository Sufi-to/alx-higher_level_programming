#!/usr/bin/python3
"""This is a unnitest for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unnitest for max_integer function."""

    def test_mod_doc(self):
        """Check for module docstring."""
        doc = __import__('6-max_integer').__doc__
        self.assertTrue(len(doc) > 1)

    def test_fun_doc(self):
        """Check for function docstring."""
        doc = __import__("6-max_integer").__doc__
        self.assertTrue(len(doc) > 1)

    def test_arg(self):
        """Check if no argument is given."""
        self.assertIsNone(max_integer())

    def test_one_arg(self):
        """Check if one element is in list."""
        my_list = [3]
        self.assertEqual(max_integer(my_list), 3)

    def test_max_last(self):
        """Check when max is last."""
        my_list = [1, 3, 5, 7]
        self.assertEqual(max_integer(my_list), 7)

    def test_max_integer(self):
        """Check max at the beginning."""
        my_list = [19, 12, 1, 5]
        self.assertEqual(max_integer(my_list), 19)

    def test_max_middle(self):
        """Check for max when it is in the middle."""
        my_list = [4, 8, 10, 4, 0]
        self.assertEqual(max_integer(my_list), 10)

    def test_max_negative(self):
        """Check for max when it is negative."""
        my_list = [-3, -4, -9, -2, -1]
        self.assertEqual(max_integer(my_list), -1)

    def test_non_int(self):
        """Check for max when there is a non int element."""
        my_list = [1, 4, 5, "he", 4]
        with self.assertRaises(TypeError):
            max_integer(my_list)

    def test_None(self):
        """Check when None is give as an arg."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
