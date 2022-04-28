import unittest
from data_structures.hashset import HashSet


def show_bucket(head):
    '''Converted a linked list to a list'''
    values = list()
    while head:
        values.append(head.value)
        head = head.next

    return values

def show_hashset(hashmap):
    '''Converted a hashmap to a list of buckets'''
    buckets = list()
    for bucket in hashmap.buckets:
        if bucket.size == 0:
            buckets.append(None)
        else:
            buckets.append(show_bucket(bucket.head))

    return buckets


class HashSetTest(unittest.TestCase):

    def test_size_hashset(self):
        hashset = HashSet()
        self.assertEqual(hashset.size, 100)

    def test_empty_hashset(self):
        hashset = HashSet(5)
        self.assertEqual(show_hashset(hashset), [None, None, None, None, None])

    def test_set_key(self):
        hashset = HashSet(5)
        hashset.add(1)
        self.assertEqual(show_hashset(hashset), [None, [1], None, None, None])

    def test_get_value(self):
        hashset = HashSet(5)
        hashset.add(1)
        value = hashset.get(1)
        self.assertEqual(show_bucket(value.head), [1])

    def test_set_same_hash(self):
        hashset = HashSet(5)
        hashset.add(1)
        hashset.add(11)
        self.assertEqual(show_hashset(hashset), [None, [1, 11], None, None, None])

    def test_get_same_hash(self):
        hashset = HashSet(5)
        hashset.add(1)
        hashset.add(11)
        value = hashset.get(11)
        self.assertEqual(show_bucket(value.head), [1, 11])


if __name__ == '__main__':
    unittest.main()
