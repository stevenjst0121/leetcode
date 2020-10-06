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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        self.levelOrderHelper(root, 0, result)
        return result

    def levelOrderHelper(self, root: TreeNode, depth: int, result: List[List[int]]) -> None:
        """
        Recursion, keep track of depth
        """
        if not root:
            return

        if len(result) <= depth:
            result.append([])
        result[depth].append(root.val)

        if root.left:
            self.levelOrderHelper(root.left, depth + 1, result)
        if root.right:
            self.levelOrderHelper(root.right, depth + 1, result)

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     """
    #     Use queue, space O(k), where k is the maximum width
    #     """
    #     if not root:
    #         return None

    #     result = []
    #     queue = deque()
    #     queue.appendleft(root)
    #     while queue:
    #         row = []
    #         for _ in range(len(queue)):
    #             node = queue.pop()
    #             row.append(node.val)
    #             if node.left:
    #                 queue.appendleft(node.left)
    #             if node.right:
    #                 queue.appendleft(node.right)
    #         result.append(row)

    #     return result
