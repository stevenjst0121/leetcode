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
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # """Recursive"""
        # result = []
        # self.preorderTraversalRecursive(root, result)
        # return result

        """Iterative DFS"""
        if not root:
            return []

        stack = deque()
        stack.append(root)
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return result

        # """Morris"""
        # result = []
        # curr = root
        # while curr:
        #     result.append(curr.val)
        #     if not curr.left:
        #         curr = curr.right
        #     else:
        #         pre = curr.left
        #         while pre.right:
        #             pre = pre.right
        #         pre.right = curr.right
        #         curr = curr.left
        # return result

    def preorderTraversalRecursive(self, root: TreeNode, res: List[int]) -> None:
        if not root:
            return

        res.append(root.val)
        self.preorderTraversalRecursive(root.left, res)
        self.preorderTraversalRecursive(root.right, res)
