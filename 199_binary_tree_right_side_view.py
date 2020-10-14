# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = deque()
        if root:
            queue.appendleft(root)

        result = []
        while queue:
            size = len(queue)
            # first is result
            for i in range(size):
                node = queue.pop()
                if i == 0:
                    result.append(node.val)
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)

        return result
