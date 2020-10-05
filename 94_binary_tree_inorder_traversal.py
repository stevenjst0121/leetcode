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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # """Recursive
        # This is pretty much the same as using stack, as recursion works as storing the value automatically
        # """
        # result = []
        # self.inorderTraversalRecursive(root, result)
        # return result

        """[MEMO] Iterative"""
        result = []
        stack = deque()
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
                continue

            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

        # """[MEMO] Morris Inorder"""
        # result = []
        # curr = root
        # while curr:
        #     if not curr.left:
        #         result.append(curr.val)
        #         curr = curr.right
        #     else:
        #         pre = curr.left
        #         while pre.right:
        #             pre = pre.right
        #         pre.right = curr
        #         temp = curr
        #         curr = curr.left
        #         temp.left = None
        # return result

    def inorderTraversalRecursive(self, root: TreeNode, res: List[int]) -> None:
        """Recursive"""
        if not root:
            return

        self.inorderTraversalRecursive(root.left, res)
        res.append(root.val)
        self.inorderTraversalRecursive(root.right, res)
