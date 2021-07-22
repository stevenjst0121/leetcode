from collections import defaultdict


class Solution:
    def __init__(self):
        self.hashmap = defaultdict(dict)

    def put(self, key: str, ts: int, val: int) -> None:
        self.hashmap[key][ts] = val

    def get(self, key: str, ts: int) -> int:
        if key not in self.hashmap or not self.hashmap[key]:
            return None

        value_dict = self.hashmap[key]
        largest_smaller = (float("-Inf"), None)
        for val_ts, val in value_dict.items():
            if val_ts <= ts and largest_smaller[0] < val_ts:
                largest_smaller = (val_ts, val)

        return largest_smaller[1]


def test_empty_map():
    solution = Solution()
    assert solution.get("A", 0) == None
    assert solution.get("B", 0) == None


def test_one_ts():
    solution = Solution()
    solution.put("A", 0, 0)
    assert solution.get("A", 0) == 0
    assert solution.get("A", 2) == 0


def test_two_ts():
    solution = Solution()
    solution.put("A", 0, 0)
    solution.put("A", 2, 2)
    assert solution.get("A", 0) == 0
    assert solution.get("A", 1) == 0
    assert solution.get("A", 2) == 2
    assert solution.get("A", 3) == 2


def test_two_key():
    solution = Solution()
    solution.put("A", 0, 0)
    solution.put("B", 2, 2)
    assert solution.get("A", 0) == 0
    assert solution.get("A", 5) == 0
    assert solution.get("B", 0) == None
    assert solution.get("B", 2) == 2
    assert solution.get("B", 5) == 2
