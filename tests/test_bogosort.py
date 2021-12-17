import unittest
from algorithms.sorting.bogosort import bogosort


class BogoSortTest(unittest.TestCase):
    def test_bogosort_sample(self):
        self.assertEqual(bogosort([5, 10, 1]), [1, 5, 10])

    def test_bogosort_with_positive_numbers(self):
        self.assertEqual(bogosort([5, 5, 7, 8, 2, 4, 1]),
                         [1, 2, 4, 5, 5, 7, 8])

    def test_bogosort_negative_numbers(self):
        self.assertEqual(bogosort([-1, -3, -5, -7, -9, -5]),
                         [-9, -7, -5, -5, -3, -1])

    def test_bogosort_with_negative_and_positive_numbers(self):
        self.assertEqual(bogosort([-6, -5, -4, 0, 5, 5, 7, 8, 2, 4, 1]),
                         [-6, -5, -4, 0, 1, 2, 4, 5, 5, 7, 8])

    def test_bogosort_same_numbers(self):
        self.assertEqual(bogosort([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_bogosort_empty_list(self):
        self.assertEqual(bogosort([]), [])


if __name__ == '__main__':
    unittest.main()
