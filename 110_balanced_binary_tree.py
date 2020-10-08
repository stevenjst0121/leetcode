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
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        is_balanced, _ = self.getHeight(root)
        return is_balanced

    def getHeight(self, root: TreeNode) -> Tuple[bool, int]:
        """Returns (If the current node is balanced, the height of current node)"""
        if not root:
            return (True, 0)

        if not root.left and not root.right:
            return (True, 1)

        is_balanced_l, height_l = self.getHeight(root.left)
        if not is_balanced_l:
            return (False, -1)
        is_balanced_r, height_r = self.getHeight(root.right)
        if not is_balanced_r:
            return (False, -1)

        if abs(height_l - height_r) > 1:
            return (False, -1)

        return (True, max(1 + height_l, 1 + height_r))
