import pytest
from typing import *
from collections import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """"""
        return self.searchHelper(nums, 0, len(nums) - 1, target)

    def searchHelper(self, nums: List[int], start: int, end: int, target: int) -> int:
        if start > end:
            return -1

        mid = start + int((end - start) / 2)
        has_pivot = False
        if nums[end] < nums[start]:
            has_pivot = True

        if nums[mid] != target:
            if has_pivot:
                res = self.searchHelper(nums, start, mid - 1, target)
                if res < 0:
                    return self.searchHelper(nums, mid + 1, end, target)
                else:
                    return res
            else:
                if nums[mid] > target:
                    return self.searchHelper(nums, start, mid - 1, target)
                else:
                    return self.searchHelper(nums, mid + 1, end, target)
        else:
            return mid


@pytest.mark.parametrize(
    "test_input,expected",
    [(([4, 5, 6, 7, 0, 1, 2], 0), 4)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.search(test_input[0], test_input[1]) == expected
