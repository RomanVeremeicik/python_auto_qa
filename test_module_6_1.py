import unittest
from module6_1 import mod1


class TestStringMethods(unittest.TestCase):
    """Тесты для функции mod1 из модуля module_6.1"""

    def test_mod1(self):
        self.assertEqual(mod1([1, 5, 6, 9]), "positive number in list")


if __name__ == '__main__':
    unittest.main()
