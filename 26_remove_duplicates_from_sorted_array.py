import pytest
from typing import *
from collections import *


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        i = 0
        for j in range(len(nums)):
            if j == 0 or nums[j - 1] != nums[j]:
                nums[i] = nums[j]
                i += 1

        return i


@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 1, 2], 2), ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.removeDuplicates(test_input) == expected
