import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 5), 10)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 4), 1)
