import pytest
from typing import *
from collections import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Be careful about duplicates
        """
        nums.sort()  # o(nLog(n))
        results = []
        i = 0
        while i < len(nums) - 2:
            x = nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = x + nums[j] + nums[k]
                if sum == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    # Here we only need to worry about one side really, as long as one side is changed
                    # the other will keep changing in the loop
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    j += 1

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return results


@pytest.mark.parametrize(
    "test_input,expected",
    [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.threeSum(test_input) == expected
