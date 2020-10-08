import pytest
from typing import *
from collections import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_list(list: List) -> ListNode:
    dummyHead = ListNode()
    curr = dummyHead
    for val in list:
        curr.next = ListNode(val)
        curr = curr.next
    return dummyHead.next


class Solution:
    """
    1. Figure out a brute force recursive solution, e.g. using nums[:i], nums[i + 1 :]
    2. Optimize 1 with memoization, introduce start and end, and store (start, end) -> result
    3. In fact, start and end does not matter, only the size of array matters
    *. See solution for tabulation DP solution, which requires some math deduction
    """

    def numTrees(self, n: int) -> int:
        memo = {}  # maps from n -> num
        return self.helper(n, memo)

    def helper(self, n: int, memo: Dict[int, int]) -> int:
        """
        Given n consecutive numbers, return how many possible BSTs
        """
        if n <= 0:
            return 0

        if n == 1:
            return 1

        sum = 0
        m = 0
        while m < n:
            if m in memo.keys():
                left = memo[m]
            else:
                left = self.helper(m, memo)
                memo[m] = left

            if n - m - 1 in memo.keys():
                right = memo[n - m - 1]
            else:
                right = self.helper(n - m - 1, memo)
                memo[n - m - 1] = right

            if left == 0 or right == 0:
                sum += left + right
            else:
                sum += left * right

            m += 1

        memo[n] = sum
        return sum

    # def numTrees(self, n: int) -> int:
    #     nums = [num for num in range(1, n + 1)]
    #     memo = {}  # maps from (start, end) -> num
    #     return self.helper(nums, 0, n - 1, memo)

    # def helper(self, nums: List[int], start: int, end: int, memo: Dict[Tuple, int]) -> int:
    #     """
    #     Given a list of nums from start to end in list nums, return how many possible BSTs
    #     """
    #     if start > end:
    #         return 0

    #     if start == end:
    #         return 1

    #     if (start, end) in memo.keys():
    #         return memo[(start, end)]

    #     sum = 0
    #     curr = start
    #     while curr <= end:
    #         if (start, curr - 1) in memo.keys():
    #             left = memo[(start, curr - 1)]
    #         else:
    #             left = self.helper(nums, start, curr - 1, memo)
    #             memo[(start, curr - 1)] = left

    #         if (curr + 1, end) in memo.keys():
    #             right = memo[(curr + 1, end)]
    #         else:
    #             right = self.helper(nums, curr + 1, end, memo)
    #             memo[(curr + 1, end)] = right

    #         if left == 0 or right == 0:
    #             sum += left + right
    #         else:
    #             sum += left * right

    #         curr += 1

    #     memo[(start, end)] = sum
    #     return sum


@pytest.mark.parametrize(
    "test_input,expected",
    [(3, 5)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.numTrees(test_input) == expected
