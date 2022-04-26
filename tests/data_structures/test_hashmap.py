import unittest
from data_structures.hashmap import HashMap


class HashMapTest(unittest.TestCase):

    def test_size_hashmap(self):
        hashmap = HashMap()
        self.assertEqual(hashmap.size, 100)

    def test_empty_hashmap(self):
        hashmap = HashMap(5)
        self.assertEqual(str(hashmap), '[], [], [], [], []')

    def test_set_key(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        self.assertEqual(str(hashmap), "[], [(1, 'value_1')], [], [], []")

    def test_get_value(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        value = hashmap[1]
        self.assertEqual(value, 'value_1')

    def test_set_same_hash(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        hashmap[11] = 'value_2'
        self.assertEqual(str(hashmap), "[], [(1, 'value_1'), (11, 'value_2')], [], [], []")

    def test_get_same_hash(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        hashmap[11] = 'value_2'
        value = hashmap[11]
        self.assertEqual(value, 'value_2')

    def test_del_key(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        self.assertEqual(str(hashmap), "[], [(1, 'value_1')], [], [], []")
        del hashmap[1]
        self.assertEqual(str(hashmap), '[], [], [], [], []')

    def test_del_key_same_hash(self):
        hashmap = HashMap(5)
        hashmap[1] = 'value_1'
        hashmap[11] = 'value_2'
        self.assertEqual(str(hashmap), "[], [(1, 'value_1'), (11, 'value_2')], [], [], []")
        del hashmap[1]
        self.assertEqual(str(hashmap), "[], [(11, 'value_2')], [], [], []")


if __name__ == '__main__':
    unittest.main()
