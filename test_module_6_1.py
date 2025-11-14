"""Module providing a function printing python version."""

import unittest
from module6_1 import mod1


class TestStringMethods(unittest.TestCase):
    """Tests for function mod1 from module_6.1"""

    def test_mod1(self):
        """test for positive numbers"""
        self.assertEqual(mod1([1, 5, 6, 9]), "positive number in list")

    def test_mod1_1(self):
        """test for negative numbers"""
        self.assertEqual(mod1([-1, 5, -6, 9]), "negative number in list")


if __name__ == '__main__':
    unittest.main()
