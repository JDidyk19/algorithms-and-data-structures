import unittest
from data_structures.hashmap import HashMap


def show_bucket(head):
    '''Converted a linked list to a list'''
    values = list()
    while head:
        values.append(head.value)
        head = head.next

    return values

def show_hashmap(hashmap):
    '''Converted a hashmap to a list of buckets'''
    buckets = list()
    for bucket in hashmap.buckets:
        if bucket.size == 0:
            buckets.append(None)
        else:
            buckets.append(show_bucket(bucket.head))

    return buckets


class HashMapTest(unittest.TestCase):

    def test_size_hashmap(self):
        hashmap = HashMap()
        self.assertEqual(hashmap.size, 100)

    def test_empty_hashmap(self):
        hashmap = HashMap(5)
        self.assertEqual(show_hashmap(hashmap), [None, None, None, None, None])

    def test_set_key(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        self.assertEqual(show_hashmap(hashmap), [None, [(1, 'value_1')], None, None, None])

    def test_get_value(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        value = hashmap[1]
        self.assertEqual(show_bucket(value.head), [(1, 'value_1')])

    def test_set_same_hash(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        hashmap[11] = 'value_11'
        self.assertEqual(show_hashmap(hashmap), [None, [(1, 'value_1'), (11, 'value_11')], None, None, None])

    def test_get_same_hash(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        hashmap[11] = 'value_11'
        value = hashmap[11]
        self.assertEqual(show_bucket(value.head), [(1, 'value_1'), (11, 'value_11')])


if __name__ == '__main__':
    unittest.main()
