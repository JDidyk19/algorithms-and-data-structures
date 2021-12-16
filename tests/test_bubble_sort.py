import unittest
import random
from algorithms.sorting.bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubble_sort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_negative_numbers(self):
        self.assertEqual(bubble_sort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_bubble_sort_with_negative_and_positive_numbers(self):
        self.assertEqual(bubble_sort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bubble_sort_same_numbers(self):
        self.assertEqual(bubble_sort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_bubble_sort_random_numbers(self):
        array = [random.randint(-100, 100) for _ in range(101)]
        sorted_array = sorted(array)
        self.assertEqual(bubble_sort(array), sorted_array)


if __name__ == '__main__':
    unittest.main()