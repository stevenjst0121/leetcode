import pytest
from typing import *
from collections import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, 0, 3, 0)

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, 0, 4, target)

    def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
        """
        Note: [MEMO] the way to handle duplicates this way with two pointers solution
        Note: [MEMO] the way to reduce work with the initial check below in sorted array
        """
        results = []
        if len(nums) - start < 2 or nums[start] * 2 > target or nums[-1] * 2 < target:
            return results

        lo = start
        hi = len(nums) - 1
        while lo < hi:
            sum = nums[lo] + nums[hi]
            if sum < target or (lo > start and nums[lo - 1] == nums[lo]):
                lo += 1
            elif sum > target or (hi < len(nums) - 1 and nums[hi + 1] == nums[hi]):
                hi -= 1
            else:
                results.append([nums[lo], nums[hi]])
                lo += 1
                hi -= 1
        return results

    def kSum(self, nums: List[int], start: int, k: int, target: int) -> List[List[int]]:
        """
        Note: [MEMO] the way to handle duplicates this way with two pointers solution
        Note: [MEMO] the way to reduce work with the initial check below in sorted array
        """
        results = []
        if len(nums) - start < k or nums[start] * k > target or nums[-1] * k < target:
            return results

        if k == 2:
            return self.twoSum(nums, start, target)

        for i in range(start, len(nums) - k + 1):
            if i == start or nums[i - 1] != nums[i]:
                for res in self.kSum(nums, i + 1, k - 1, target - nums[i]):
                    results.append([nums[i]] + res)
        return results


@pytest.mark.parametrize(
    "test_input,expected",
    [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])],
)
def test_3_sum(test_input, expected):
    s = Solution()
    assert s.threeSum(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 0, -1, 0, -2, 2], [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])],
)
def test_4_sum(test_input, expected):
    s = Solution()
    assert s.fourSum(test_input, 0) == expected


if __name__ == "__main__":
    s = Solution()
    test = [1, 2, 4, 5, 7]
    print(s.twoSum(test, 0, 6))
