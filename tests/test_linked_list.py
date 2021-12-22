import unittest
from data_structures.linked_list import LinkedList


def to_list(l_list: LinkedList) -> list:
    array = list()
    current_node = l_list.head
    while current_node:
        array.append(current_node.value)
        current_node = current_node.next
    return array


class LinkedListTest(unittest.TestCase):
    def test_is_empty_list_true(self):
        l_list = LinkedList()
        self.assertEqual(l_list.is_empty(), True)

    def test_is_empty_list(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(3)
        self.assertEqual(l_list.is_empty(), False)

    def test_push_front(self):
        l_list = LinkedList()
        l_list.push_front(1).push_front(2).push_front(3)
        self.assertEqual(to_list(l_list), [3, 2, 1])

    def test_push_back(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(3)
        self.assertEqual(to_list(l_list), [1, 2, 3])

    def test_pop_front(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(3)
        el = l_list.pop_front()
        self.assertEqual(el, 1)
        self.assertEqual(to_list(l_list), [2, 3])

    def test_pop_back(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(3)
        el = l_list.pop_back()
        self.assertEqual(el, 3)
        self.assertEqual(to_list(l_list), [1, 2])

    def test_pop_front_one_element(self):
        l_list = LinkedList()
        l_list.push_back(1)
        el = l_list.pop_front()
        self.assertEqual(el, 1)
        self.assertEqual(to_list(l_list), [])

    def test_pop_front_back_empty_list(self):
        l_list = LinkedList()
        el = l_list.pop_front()
        self.assertEqual(el, None)

    def test_pop_back_one_element(self):
        l_list = LinkedList()
        l_list.push_back(1)
        el = l_list.pop_back()
        self.assertEqual(el, 1)
        # self.assertEqual(to_list(l_list), [])

    def test_top_front(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(3)
        self.assertEqual(l_list.top_front(), 1)

    def test_top_back(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(3)
        self.assertEqual(l_list.top_back(), 3)

    def test_top_front_back_one_element(self):
        l_list = LinkedList()
        l_list.push_back(1)
        self.assertEqual(l_list.top_front(), 1)
        self.assertEqual(l_list.top_back(), 1)

    def test_top_front_back_empty_list(self):
        l_list = LinkedList()
        self.assertEqual(l_list.top_front(), None)
        self.assertEqual(l_list.top_back(), None)

    def test_find_true(self):
        l_list = LinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        self.assertEqual(l_list.find(4), True)

    def test_find_false(self):
        l_list = LinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        self.assertEqual(l_list.find(6), False)

    def test_find_empty_list(self):
        l_list = LinkedList()
        self.assertEqual(l_list.find(4), False)

    def test_erase(self):
        l_list = LinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        l_list.erase(5)
        self.assertEqual(to_list(l_list), [1, 2, 3, 4])

    def test_erase_more_the_same_elements(self):
        l_list = LinkedList()
        l_list.push_back(1).push_back(2).push_back(2).push_back(2).push_back(3).push_back(4).push_back(5)
        l_list.erase(2)
        self.assertEqual(to_list(l_list), [1, 3, 4, 5])

    def test_erase_empty_list(self):
        l_list = LinkedList()
        self.assertEqual(l_list.erase(1), None)

    def test_size_list(self):
        l_list = LinkedList()
        for num in range(1, 6):
            l_list.push_back(num)

        self.assertEqual(l_list.size(), 5)


if __name__ == '__main__':
    unittest.main()

