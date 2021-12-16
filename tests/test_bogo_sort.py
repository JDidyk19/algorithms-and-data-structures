import unittest
from algorithms.sorting.bogo_sort import bogo_sort


class BogoSortTest(unittest.TestCase):
    def test_bogo_sort_with_positive_numbers(self):
        self.assertEqual(bogo_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_bogo_sort_negative_numbers(self):
        self.assertEqual(bogo_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_bogo_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(bogo_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bogo_sort_same_numbers(self):
        self.assertEqual(bogo_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_bogo_sort_empty_list(self):
        self.assertEqual(bogo_sort([]), [])


if __name__ == '__main__':
    unittest.main()
