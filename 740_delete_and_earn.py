from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """Solution
        Brilliant bottom-up DP solution
        Using the fact that when taking a number k, we might just take all ks together
        [MEMO] Use Counter + sorted()
        """
        count = Counter(nums)
        prev = None
        avoid, using = 0, 0
        for k in sorted(count):
            new_avoid = max(avoid, using)
            if k - 1 == prev:
                new_using = k * count[k] + avoid
            else:
                new_using = k * count[k] + max(avoid, using)
            prev = k
            avoid = new_avoid
            using = new_using
        return max(avoid, using)

    def __init__(self):
        self.memo = {}  # nums -> points

    def deleteAndEarn(self, nums: List[int]) -> int:
        """Draft 1
        Standard Top-down DP, works but exceeds time limit
        """
        if not nums:
            return 0

        key = tuple(nums)
        if key in self.memo:
            return self.memo[key]

        max_points = float("-Inf")
        for i, points in enumerate(nums):
            sub_nums = [
                num for num in nums[:i] + nums[i + 1 :] if num != points - 1 and num != points + 1
            ]
            sub_points = self.deleteAndEarn(sub_nums)
            total_points = points + sub_points
            if total_points > max_points:
                max_points = total_points

        self.memo[key] = max_points
        return max_points
