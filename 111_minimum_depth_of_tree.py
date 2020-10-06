import sys
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
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        min = sys.maxsize
        stack = deque()
        stack.append(root)
        height = 1
        while stack:
            for _ in range(len(stack)):
                node = stack.pop()
                if not node.left and not node.right:
                    # leaf
                    if height < min:
                        min = height
                    continue

                if node.left:
                    stack.appendleft(node.left)
                if node.right:
                    stack.appendleft(node.right)
            height += 1

        return min
