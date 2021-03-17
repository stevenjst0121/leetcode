import pytest
from typing import *
from collections import *


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        [MEMO] Keep a map of sums, where sums[num] = the number of times sum (calculated from index 0) has occured
        Iterate through nums and keep tracking of current sum since index 0
        Use the iterator as the END of a possible subarray, find how many times sums[sum - k] has occurred
            (sum - k) + k = sum, where k is the subarray we are looking for
        """
        count = 0
        sums = defaultdict(int)
        sums[0] = 1  # empty list
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            count += sums[sum - k]
            sums[sum] += 1
        return count

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """
    #     Bring in the concept of cumulative array, but still exceeds time due to O(n^2)
    #     """
    #     sums = {}
    #     sums[0] = 0
    #     count = 0
    #     for i in range(len(nums)):
    #         sums[i + 1] = sums[i] + nums[i]

    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums) + 1):
    #             if sums[j] - sums[i] == k:
    #                 count += 1
    #     return count

    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     """Brute Force
    #     Be careful for cases:
    #     1. Chosen number itself is good already
    #     2. There could be multiple results for a starting point value
    #     """
    #     count = 0
    #     for i in range(len(nums)):
    #         sum = nums[i]
    #         if sum == k:
    #             count += 1

    #         j = i + 1
    #         while j < len(nums):
    #             sum += nums[j]
    #             if sum == k:
    #                 count += 1

    #             j += 1
    #     return count


@pytest.mark.parametrize(
    "test_input,expected",
    [(([1, 1, 1], 2), 2), (([-1, -1, 1], 0), 1), (([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0), 55)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.subarraySum(test_input[0], test_input[1]) == expected
