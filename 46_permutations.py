from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """Solution
        [MEMO] backtrack to find all possible solutions
        47_permutations_2 solution is better and can handle dups too!!!
        """
        self.result = []
        self.backtrack(nums, 0)
        return self.result

    def backtrack(self, nums: List[int], first: int):
        N = len(nums)
        if first == N:
            self.result.append(nums.copy())
        for i in range(first, N):
            nums[first], nums[i] = nums[i], nums[first]
            self.backtrack(nums, first + 1)
            nums[first], nums[i] = nums[i], nums[first]
