from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        [MEMO] backtrack, kind of like DP that builds comp from 0
        """
        self.N = len(nums)
        self.result = []
        self.backtrack([], Counter(nums))
        return self.result

    def backtrack(self, comb, counter):
        if len(comb) == self.N:
            self.result.append(comb.copy())
            return

        for num in counter:
            if counter[num] > 0:
                comb.append(num)
                counter[num] -= 1
                self.backtrack(comb, counter)
                comb.pop()
                counter[num] += 1