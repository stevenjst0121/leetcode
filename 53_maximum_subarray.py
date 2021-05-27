from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * N
        dp[-1] = nums[-1]
        max_sub = dp[-1]
        for i in range(N - 2, -1, -1):
            if dp[i + 1] > 0:
                dp[i] = dp[i + 1] + nums[i]
            else:
                dp[i] = nums[i]

            if dp[i] > max_sub:
                max_sub = dp[i]
        return max_sub

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
