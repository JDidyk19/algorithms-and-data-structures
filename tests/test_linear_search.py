import unittest
from algorithms.search.linear_search import linear_search


class LinearSearchTest(unittest.TestCase):
    def test_1(self):
        array = [10, 2, 5, 10, 1, 2]
        self.assertEqual(linear_search(1, array), 4)

    def test_2(self):
        array = [100, 35, 10, 450, 1000, 34, 1, 4, 9, 15, 20, 45, 129]
        self.assertEqual(linear_search(129, array), 12)

    def test_3(self):
        array = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
        self.assertEqual(linear_search(10, array), -1)

    def test_4(self):
        array = [10, 14, 16, 7, 90, 489, 34, 100, 5678, 123, 453, 456, 190, 47875, 567, 108, 789]
        self.assertEqual(linear_search(1250, array), -1)


if __name__ == '__main__':
    unittest.main()