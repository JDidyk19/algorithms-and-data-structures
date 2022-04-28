from data_structures.linked_list import LinkedList


class HashSet:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [LinkedList() for _ in range(self.size)]

    def add(self, key):
        hash_key = hash(key) % self.size
        bucket = self.buckets[hash_key]
        bucket.push_back(key)

    def get(self, key):
        hash_key = hash(key) % self.size
        bucket = self.buckets[hash_key]
        return bucket
