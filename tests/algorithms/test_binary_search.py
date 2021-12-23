import unittest
from algorithms.search.binary_search import binary_search_iterative, binary_search_recursive


class BinarySearchTest(unittest.TestCase):
    def test_first_element(self):
        array = list(range(1000))
        self.assertEqual(binary_search_iterative(array, 0), 0)
        self.assertEqual(binary_search_recursive(array, 0), 0)

    def test_middle_element(self):
        array = list(range(1000))
        self.assertEqual(binary_search_iterative(array, 123), 123)
        self.assertEqual(binary_search_recursive(array, 123), 123)

    def test_last_element(self):
        array = list(range(1000))
        self.assertEqual(binary_search_iterative(array, 999), 999)
        self.assertEqual(binary_search_recursive(array, 999), 999)

    def test_empty_list(self):
        array = list()
        self.assertEqual(binary_search_iterative(array, 100), -1)
        self.assertEqual(binary_search_recursive(array, 100), -1)

    def test_element_not_in_list(self):
        array = list(range(1000))
        self.assertEqual(binary_search_iterative(array, 1000), -1)
        self.assertEqual(binary_search_recursive(array, 1000), -1)

    def test_random_elements(self):
        array = [14, 23, 121, 146, 159, 328, 361, 388, 606, 628, 637, 668, 703, 704, 729, 729, 816, 878, 889, 976]
        self.assertEqual(binary_search_iterative(array, 628), 9)
        self.assertEqual(binary_search_recursive(array, 628), 9)


if __name__ == '__main__':
    unittest.main()
