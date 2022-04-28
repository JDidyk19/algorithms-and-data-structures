from data_structures.linked_list import LinkedList


class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [LinkedList() for _ in range(self.size)]

    def __get_hash(self, key):
        return hash(key) % self.size

    def __getitem__(self, key):
        hashed_key = self.__get_hash(key)
        bucket = self.buckets[hashed_key]
        return bucket

    def __setitem__(self, key, val):
        hashed_key = self.__get_hash(key)
        bucket = self.buckets[hashed_key]
        bucket.push_back((key, val))
