from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """Draft 1
        Trick is to store module of 60 to dict and calculate while looping
        """
        times = defaultdict(int)
        result = 0

        for t in time:
            res = t % 60
            diff = (60 - res) % 60
            if diff in times:
                result += times[diff]

            times[res] += 1
        return result
