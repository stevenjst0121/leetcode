# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        [MEMO] Draft 1, same as solution 1, O(N), 70%
        """
        self.lca = None
        self.dfs(root, p, q)
        return self.lca

    def dfs(self, node, p, q):
        # Return true/false indicating if p/q is in sub-tree of this node
        if not node:
            return False

        if self.lca:
            # lca already found
            return False

        is_p_q = False
        if node.val == p.val or node.val == q.val:
            is_p_q = True

        left_res = self.dfs(node.left, p, q)
        right_res = self.dfs(node.right, p, q)

        if self.lca:
            return True

        if is_p_q:
            if left_res or right_res:
                self.lca = node
            return True

        if left_res and right_res:
            self.lca = node
            return True

        return left_res or right_res
