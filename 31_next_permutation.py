import pytest
from typing import *
from collections import *


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """"""
        if not self.nextPermutationHelper(nums, len(nums) - 2):
            nums.sort()

    def nextPermutationHelper(self, nums: List[int], start: int) -> bool:
        """
        Returns true if next permutation exist
        """
        if start < 0:
            return False

        least_bigger_pos = -1
        for i in range(start + 1, len(nums)):
            if nums[i] > nums[start] and (least_bigger_pos < 0 or nums[i] < nums[least_bigger_pos]):
                least_bigger_pos = i

        if least_bigger_pos > 0:
            nums[start], nums[least_bigger_pos] = nums[least_bigger_pos], nums[start]
            nums[start + 1 :] = sorted(nums[start + 1 :])
            return True
        else:
            return self.nextPermutationHelper(nums, start - 1)


@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 2, 3], [1, 3, 2]), ([3, 2, 1], [1, 2, 3]), ([1, 1, 5], [1, 5, 1])],
)
def test_solution(test_input, expected):
    s = Solution()
    s.nextPermutation(test_input)
    assert test_input == expected
