"""
Traverse through tree (DFS) does NOT require memoization!!!
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        [MEMO] Get depth while calculating max diameter_
        """
        self.max_diameter = 0
        self.getDepth(root)
        return self.max_diameter

    def getDepth(self, node: TreeNode) -> int:
        if not node:
            return 0

        l_depth = self.getDepth(node.left)
        r_depth = self.getDepth(node.right)
        diameter = l_depth + r_depth
        self.max_diameter = max(self.max_diameter, diameter)
        return max(l_depth, r_depth) + 1