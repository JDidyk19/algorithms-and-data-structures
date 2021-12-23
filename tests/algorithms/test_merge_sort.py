import unittest
import random
from algorithms.sorting.merge_sort import merge_sort


class MergeSortTest(unittest.TestCase):
    def test_merge_sort_sample(self):
        self.assertEqual(merge_sort([5, 10, 1]), [1, 5, 10])

    def test_merge_sort_with_positive_numbers(self):
        self.assertEqual(merge_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_merge_sort_negative_numbers(self):
        self.assertEqual(merge_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_merge_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(merge_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_merge_sort_same_numbers(self):
        self.assertEqual(merge_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_merge_sort_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_merge_sort_random_numbers(self):
        array = [random.randint(-100, 100) for _ in range(101)]
        sorted_array = sorted(array)
        self.assertEqual(merge_sort(array), sorted_array)


if __name__ == '__main__':
    unittest.main()
