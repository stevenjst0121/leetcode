import pytest
from typing import *
from collections import *
import sys


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Note: The answer must be within the range of [1, n+1]
        Note2: Looping through an array multiple times is still O(n), as long as no nested loops
        MEMO
        https://youtu.be/9SnkdYXNIzM
        """
        has_one = False
        for i in range(len(nums)):
            if nums[i] == 1:
                has_one = True

            if nums[i] <= 0 or nums[i] > len(nums) + 1:
                nums[i] = 1

        if not has_one:
            return 1

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index < len(nums) and nums[index] > 0:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1


@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1), ([3, 1], 2)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.firstMissingPositive(test_input) == expected
