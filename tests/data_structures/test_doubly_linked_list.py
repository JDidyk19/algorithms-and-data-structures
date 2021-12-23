import unittest
from data_structures.doubly_linked_list import DoublyLinkedList


def to_list(l_list) -> list:
    """Convert a doubly linked list to a list"""
    array = list()
    current_node = l_list.head
    while current_node:
        array.append(current_node.value)
        current_node = current_node.next
    return array


class DoublyLinkedListTest(unittest.TestCase):
    def test_is_empty_list(self):
        l_list = DoublyLinkedList()
        l_list_empty = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)

        self.assertEqual(l_list.is_empty(), False)
        self.assertEqual(l_list_empty.is_empty(), True)

    def test_push_front(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_front(num)
        self.assertEqual(to_list(l_list), [4, 3, 2, 1, 0])

    def test_push_back(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)
        self.assertEqual(to_list(l_list), [0, 1, 2, 3, 4])

    def test_pop_front(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)
        el = l_list.pop_front()
        self.assertEqual(el, 0)
        self.assertEqual(to_list(l_list), [1, 2, 3, 4])

    def test_pop_back(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)
        el = l_list.pop_back()
        self.assertEqual(el, 4)
        self.assertEqual(to_list(l_list), [0, 1, 2, 3])

    def test_pop_front_one_element(self):
        l_list = DoublyLinkedList()
        l_list.push_back(1)
        el = l_list.pop_front()
        self.assertEqual(el, 1)
        self.assertEqual(to_list(l_list), [])

    def test_pop_back_one_element(self):
        l_list = DoublyLinkedList()
        l_list.push_back(1)
        el = l_list.pop_back()
        self.assertEqual(el, 1)
        self.assertEqual(to_list(l_list), [])

    def test_pop_front_pop_back_empty_list(self):
        l_list = DoublyLinkedList()
        with self.assertRaises(IndexError):
            l_list.pop_front()

        with self.assertRaises(IndexError):
            l_list.pop_back()

    def test_top_front(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)
        self.assertEqual(l_list.top_front(), 0)

    def test_top_back(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)
        self.assertEqual(l_list.top_back(), 4)

    def test_top_front_top_back_one_element(self):
        l_list = DoublyLinkedList()
        l_list.push_back(1)
        self.assertEqual(l_list.top_front(), 1)
        self.assertEqual(l_list.top_back(), 1)

    def test_top_front_top_back_empty_list(self):
        l_list = DoublyLinkedList()
        with self.assertRaises(IndexError):
            l_list.top_front()

        with self.assertRaises(IndexError):
            l_list.top_back()

    def test_find_true(self):
        l_list = DoublyLinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        self.assertEqual(l_list.find(4), True)

    def test_find_false(self):
        l_list = DoublyLinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        self.assertEqual(l_list.find(6), False)

    def test_find_empty_list(self):
        l_list = DoublyLinkedList()
        self.assertEqual(l_list.find(4), False)

    def test_erase(self):
        l_list = DoublyLinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        l_list.erase(5)
        self.assertEqual(to_list(l_list), [1, 2, 3, 4])

    def test_erase_more_the_same_elements(self):
        l_list = DoublyLinkedList()
        l_list.push_back(1).push_back(2).push_back(2).push_back(2).push_back(3).push_back(4).push_back(5)
        l_list.erase(2)
        self.assertEqual(to_list(l_list), [1, 3, 4, 5])

    def test_erase_empty_list(self):
        l_list = DoublyLinkedList()
        with self.assertRaises(IndexError):
            l_list.erase(1)

    def test_size_list(self):
        l_list = DoublyLinkedList()
        for num in range(5):
            l_list.push_back(num)

        self.assertEqual(l_list.get_size(), 5)


if __name__ == '__main__':
    unittest.main()