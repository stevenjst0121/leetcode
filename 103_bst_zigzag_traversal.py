from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.dfs(root, 0)
        return self.result

    def dfs(self, node: TreeNode, level: int):
        if not node:
            return

        if level >= len(self.result):
            self.result.append(deque())

        if level % 2 == 0:
            # left to right
            self.result[level].append(node.val)
        else:
            # right to left
            self.result[level].appendleft(node.val)

        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)