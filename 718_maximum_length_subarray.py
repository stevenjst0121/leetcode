from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """DP Solution
        [MEMO] The hard part was to think how to DP
        dp[i][j] is maximum length of starting at i in nums1 and j in nums2
        And the final result needs to get maximum of all dp[i][j]
        """
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        return max(max(row) for row in dp)
