from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """Draft 1
        Recursion
        """
        if not preorder or not inorder:
            return None

        if len(preorder) == 1 or len(inorder) == 1:
            return TreeNode(preorder[0])

        root_val = preorder[0]
        root = TreeNode(root_val)
        inorder_root_index = inorder.index(root_val)
        root.left = self.buildTree(
            preorder[1 : inorder_root_index + 1], inorder[:inorder_root_index]
        )
        root.right = self.buildTree(
            preorder[inorder_root_index + 1 :], inorder[inorder_root_index + 1 :]
        )
        return root
