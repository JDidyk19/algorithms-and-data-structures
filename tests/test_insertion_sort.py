import unittest
import random
from algorithms.sorting.insertion_sort import insertion_sort


class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort_with_positive_numbers(self):
        self.assertEqual(insertion_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_insertion_sort_negative_numbers(self):
        self.assertEqual(insertion_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_insertion_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(insertion_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_insertion_sort_same_numbers(self):
        self.assertEqual(insertion_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_insertion_sort_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_insertion_sort_random_numbers(self):
        array = [random.randint(-100, 100) for _ in range(101)]
        sorted_array = sorted(array)
        self.assertEqual(insertion_sort(array), sorted_array)


if __name__ == '__main__':
    unittest.main()
