import unittest
import calc


lista = [range(10)]

a = "andres"


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(5, 5), 10)
        self.assertEqual(calc.add(-5, 4), -1)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 4), 1)
        self.assertEqual(calc.sub(1, -1), 2)
