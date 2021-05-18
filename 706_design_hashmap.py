class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.load_factor = 1000
        self.buckets = [[] for _ in range(self.load_factor)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.load_factor
        bucket = self.buckets[index]

        # check if key exists
        key_index = -1
        for i in range(len(bucket)):
            k = bucket[i][0]
            if k == key:
                key_index = i
                break

        if key_index >= 0:
            # update
            bucket[key_index] = (key, value)
        else:
            bucket.append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.load_factor
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.load_factor
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            k = bucket[i][0]
            if k == key:
                del bucket[i]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)