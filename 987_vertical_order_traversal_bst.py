from typing import List
from collections import OrderedDict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.node_list = []

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        """Solution 1
        Was trying to build solution in sorted order while traversing, ran into difficulties since sort requires multi-dimentions
        Global order solution still beats 94%
        One can use heap to keep list sorted, but basically avoids O(NLogN) at the end with each insertion taking O(logN)
        [MEMO] You can sort 3-dimensional coordinates directly in a list of (x, y, z)
        [MEMO] Can use OrderedDict if needed, but remember its time complexities
        """
        # Traverse
        self.traverse(root, 0, 0)

        # Sort
        self.node_list.sort()

        # Output
        ret = OrderedDict()
        for x, y, val in self.node_list:
            if x in ret:
                ret[x].append(val)
            else:
                ret[x] = [val]
        return list(ret.values())

    def traverse(self, root: TreeNode, x: int, y: int) -> None:
        if not root:
            return

        self.node_list.append((x, y, root.val))
        self.traverse(root.left, x - 1, y + 1)
        self.traverse(root.right, x + 1, y + 1)
