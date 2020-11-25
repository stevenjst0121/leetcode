import pytest
from typing import *
from collections import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """Draft 2
        Divide and conqur to find a target
        +
        Divide and conqur to find min/max
        """
        index = self.searchTarget(nums, 0, len(nums) - 1, target)
        if index < 0:
            return [-1, -1]

        min = self.searchMin(nums, 0, index, target)
        max = self.searchMax(nums, index, len(nums) - 1, target)
        return [min, max]

    def searchTarget(self, nums: List[int], start: int, end: int, target: int) -> int:
        if start > end:
            return -1

        mid = start + (end - start) // 2
        num = nums[mid]
        if num == target:
            return mid

        if num > target:
            return self.searchTarget(nums, start, mid - 1, target)
        else:
            return self.searchTarget(nums, mid + 1, end, target)

    def searchMin(self, nums: List[int], start: int, end: int, target: int) -> int:
        mid = start + (end - start) // 2
        num = nums[mid]
        if num == target:
            if mid == start or nums[mid - 1] != target:
                return mid
            else:
                return self.searchMin(nums, start, mid - 1, target)
        else:
            return self.searchMin(nums, mid + 1, end, target)

    def searchMax(self, nums: List[int], start: int, end: int, target: int) -> int:
        mid = start + (end - start) // 2
        num = nums[mid]
        if num == target:
            if mid == end or nums[mid + 1] != target:
                return mid
            else:
                return self.searchMax(nums, mid + 1, end, target)
        else:
            return self.searchMax(nums, start, mid - 1, target)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Simple binary search only beats 36%
        Need to add avoid duplicates to beat 90%
        """
        return self.searchRangeHelper(nums, 0, len(nums) - 1, target)

    def searchRangeHelper(self, nums: List[int], start: int, end: int, target: int) -> List[int]:
        if start > end:
            return [-1, -1]

        mid = start + int((end - start) / 2)
        val = nums[mid]
        if nums[mid] > target:
            while mid >= 0 and nums[mid] == val:
                mid -= 1
            return self.searchRangeHelper(nums, start, mid, target)
        elif nums[mid] < target:
            while mid < len(nums) and nums[mid] == val:
                mid += 1
            return self.searchRangeHelper(nums, mid, end, target)
        else:
            # found it
            lo = mid
            while lo - 1 >= 0 and nums[lo - 1] == target:
                lo -= 1
            hi = mid
            while hi + 1 < len(nums) and nums[hi + 1] == target:
                hi += 1
            return [lo, hi]


@pytest.mark.parametrize(
    "test_input,expected",
    [(([5, 7, 7, 8, 8, 10], 8), [3, 4]), (([5, 7, 7, 8, 8, 10], 6), [-1, -1])],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.searchRange(test_input[0], test_input[1]) == expected
