import unittest
from algorithms.search.linear_search import linear_search


class LinearSearchTest(unittest.TestCase):
    def test_first_element(self):
        array = list(range(1000))
        self.assertEqual(linear_search(array, 0), 0)

    def test_middle_element(self):
        array = [10, 14, 16, 7, 90, 489, 34, 100, 5678, 123, 453, 456, 190, 47875, 567, 108, 789]
        self.assertEqual(linear_search(array, 123), 9)

    def test_last_element(self):
        array = list(range(1000))
        self.assertEqual(linear_search(array, 999), 999)

    def test_empty_list(self):
        array = list()
        self.assertEqual(linear_search(array, 100), -1)

    def test_element_not_in_list(self):
        array = list(range(1000))
        self.assertEqual(linear_search(array, 1000), -1)


if __name__ == '__main__':
    unittest.main()
