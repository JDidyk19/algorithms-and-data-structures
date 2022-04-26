class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def __get_hash(self, key):
        return hash(key) % self.size

    def __getitem__(self, key):
        hashed_key = self.__get_hash(key)
        bucket = self.buckets[hashed_key]
        for record in bucket:
            record_key, record_value = record
            if record_key == key:
                return record_value

    def __setitem__(self, key, val):
        hashed_key = self.__get_hash(key)
        bucket = self.buckets[hashed_key]
        if bucket:
            found_key = False
            for idx, record in enumerate(bucket):
                record_key, record_value = record
                if record_key == key:
                    found_key = True
                    break

            if found_key:
                bucket[idx][-1] = val
            else:
                bucket.append((key, val))

        else:
            bucket = [(key, val)]
            self.buckets[hashed_key] = bucket
        return

    def __delitem__(self, key):
        hashed_key = self.__get_hash(key)
        bucket = self.buckets[hashed_key]
        for idx, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                bucket.pop(idx)
                return

    def __str__(self):
        return ', '.join([str(bucket) for bucket in self.buckets])
