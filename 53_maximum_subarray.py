from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """DP solution - Kadane's Algorithm
        [MEMO] Determines if the current subarray is worth keeping
        """
        current_subarray = nums[0]
        max_subarray = nums[0]
        for num in nums[1:]:
            current_subarray = max(current_subarray + num, num)
            max_subarray = max(max_subarray, current_subarray)
        return max_subarray