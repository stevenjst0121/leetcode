import pytest
from typing import *
from collections import *


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """"""
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


@pytest.mark.parametrize(
    "test_input,expected",
    [(([3, 2, 2, 3], 3), 2), (([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.removeElement(test_input[0], test_input[1]) == expected
