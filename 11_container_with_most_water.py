import pytest
from typing import *
from collections import *


class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     """
    #     Recursive
    #     """
    #     return self.maxAreaHelper(height, 0, len(height) - 1)

    def maxAreaHelper(self, height: List[int], i: int, j: int) -> int:
        if i >= j:
            return 0

        area = (j - i) * min(height[i], height[j])

        if height[i] > height[j]:
            return max(area, self.maxAreaHelper(height, i, j - 1))
        else:
            return max(area, self.maxAreaHelper(height, i + 1, j))

    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_area = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            max_area = max(max_area, area)
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1

        return max_area


@pytest.mark.parametrize(
    "test_input,expected",
    [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.maxArea(test_input) == expected
