import pytest
from typing import *
from collections import *


class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     if len(nums1) < len(nums2):
    #         nums_o = nums1
    #         nums_c = nums2
    #     else:
    #         nums_o = nums2
    #         nums_c = nums1

    #     d = defaultdict(int)
    #     for num in nums_o:
    #         d[num] += 1

    #     result = []
    #     for num in nums_c:
    #         if d[num] > 0:
    #             result.append(num)
    #             d[num] -= 1
    #     return result

    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     """Follow up
    #     What if the arrays are sorted
    #     """
    #     i, j = 0, 0
    #     result = []
    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] < nums2[j]:
    #             i += 1
    #         elif nums1[i] > nums2[j]:
    #             j += 1
    #         else:
    #             result.append(nums1[i])
    #             i += 1
    #             j += 1
    #     return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Built in function"""
        return [value for value in nums1 if value in nums2]


@pytest.mark.parametrize(
    "test_input,expected",
    [(([1, 1, 2, 2], [2, 2]), [2, 2]), (([4, 5, 9], [4, 4, 8, 9, 9]), [4, 9])],
)
def test_solution(test_input, expected):
    s = Solution()
    assert Counter(s.intersect(test_input[0], test_input[1])) == Counter(expected)
