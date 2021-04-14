from collections import defaultdict
from math import ceil


class TimeMap:
    def __init__(self):
        """Draft 1
        Map + binary search (pay attention to use ceil), beats 27%

        Solution 2 suggests use a balanced BST (e.g. red-black)
        Set would O(logN) and get would also be O(logN)
        """
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        if timestamp < values[0][0]:
            return ""

        low, high = 0, len(values) - 1
        while low < high:
            mid = low + ceil((high - low) / 2)
            if values[mid][0] > timestamp:
                high = mid - 1
            else:
                low = mid
        return values[low][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)