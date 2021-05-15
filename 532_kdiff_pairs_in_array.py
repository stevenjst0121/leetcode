from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """Solution
        [MEMO] Use counter to check
        And only check num + k, this avoid duplicates automatically
        """
        counter = Counter(nums)

        result = 0

        for num in counter:
            if k > 0 and num + k in counter:
                result += 1
            elif k == 0 and counter[num] > 1:
                result += 1
        return result

    def findPairs(self, nums: List[int], k: int) -> int:
        """Draft 1
        Found a hacky to store found items in set:
            (num, "u") - means num + its upper num has been found
            (num, "l") - means num + its lower num has been found
        """
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        found = set()
        result = 0
        for i, num in enumerate(nums):
            if (num, "u") not in found:
                upper = num + k
                if (upper, "l") not in found and upper in nums_map and nums_map[upper] > i:
                    found.add((num, "u"))
                    found.add((upper, "l"))
                    result += 1

            if k != 0 and (num, "l") not in found:
                lower = num - k
                if (lower, "u") not in found and lower in nums_map and nums_map[lower] > i:
                    found.add((num, "l"))
                    found.add((lower, "u"))
                    result += 1
        return result
