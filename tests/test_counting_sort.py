import unittest
import random
from algorithms.sorting.counting_sort import counting_sort


class CountingSortTest(unittest.TestCase):
    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(counting_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_same_numbers(self):
        self.assertEqual(counting_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(counting_sort([]), [])

    def test_bubble_sort_random_positive_numbers(self):
        array = [random.randint(0, 100) for _ in range(101)]
        sorted_array = sorted(array)
        self.assertEqual(counting_sort(array), sorted_array)


if __name__ == '__main__':
    unittest.main()
