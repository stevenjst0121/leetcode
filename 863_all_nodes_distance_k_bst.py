from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """Solution 1
        [MEMO] Traverse once to find parent for each node and then do BFS starting from target node
        Beats 97%
        """
        self.dfs(root, None)
        return self.bfs(target, k)

    def dfs(self, node: TreeNode, parent: TreeNode):
        if not node:
            return

        node.parent = parent
        self.dfs(node.left, node)
        self.dfs(node.right, node)

    def bfs(self, target: TreeNode, k: int):
        queue = deque([(target, 0)])
        seen = set([target])
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]

            size = len(queue)
            for _ in range(size):
                node, d = queue.popleft()
                if node.left and node.left not in seen:
                    seen.add(node.left)
                    queue.append((node.left, d + 1))
                if node.right and node.right not in seen:
                    seen.add(node.right)
                    queue.append((node.right, d + 1))
                if node.parent and node.parent not in seen:
                    seen.add(node.parent)
                    queue.append((node.parent, d + 1))
        return []
