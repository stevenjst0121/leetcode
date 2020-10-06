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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        Use deque, so as to finding max depth while iterating
        Approach 1: Normal DFS traversal, and then reverse result - result[::-1]
        Approach 2: Keep track of maximum heigh and construct result while iterating
        Approach 3: Iteractively and then reverse result (or use max height to avoid reverse)
        """
        self.max_depth = -1
        result = deque()
        self.levelOrderBottomHelper(root, 0, result)
        return list(result)

    def levelOrderBottomHelper(self, root: TreeNode, depth: int, result: Deque[List[int]]) -> None:
        if not root:
            return

        if len(result) <= depth:
            result.appendleft([])
        if self.max_depth < depth:
            self.max_depth = depth

        if root.left:
            self.levelOrderBottomHelper(root.left, depth + 1, result)
        if root.right:
            self.levelOrderBottomHelper(root.right, depth + 1, result)

        level = self.max_depth - depth
        result[level].append(root.val)
