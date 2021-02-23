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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        Traverse tree in reverse order and store result in reverse order
        """
        if not root:
            return []

        result = deque()
        curr = root
        stack = deque()
        while curr or stack:
            if curr:
                result.appendleft(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()
        return list(result)
