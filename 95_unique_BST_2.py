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
    def generateTrees(self, n: int) -> List[TreeNode]:
        nums = [num for num in range(1, n + 1)]
        memo = {}  # Maps from (start, end) -> [TreeNode]
        return self.helper(nums, 0, n - 1, memo)

    def helper(self, nums: List[int], start: int, end: int, memo) -> List[TreeNode]:
        if start > end:
            return []

        if start == end:
            return [TreeNode(nums[start])]

        if (start, end) in memo.keys():
            return memo[(start, end)]

        results = []
        curr = start
        while curr <= end:
            if (start, curr - 1) in memo.keys():
                left = memo[(start, curr - 1)]
            else:
                left = self.helper(nums, start, curr - 1, memo)
                memo[(start, curr - 1)] = left

            if (curr + 1, end) in memo.keys():
                right = memo[(curr + 1, end)]
            else:
                right = self.helper(nums, curr + 1, end, memo)
                memo[(curr + 1, end)] = right

            if not left:
                for node in right:
                    root = TreeNode(nums[curr])
                    root.right = node
                    results.append(root)
            elif not right:
                for node in left:
                    root = TreeNode(nums[curr])
                    root.left = node
                    results.append(root)
            else:
                for l_node in left:
                    for r_node in right:
                        root = TreeNode(nums[curr])
                        root.left = l_node
                        root.right = r_node
                        results.append(root)
            curr += 1

        memo[(start, end)] = results
        return results