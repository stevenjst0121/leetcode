# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        """
        [MEMO] If there is order requirement like top to bottom && left to right
        Always use BFS
        [Tip] Can always sort the keys and then output
        """
        if not root:
            return []

        min_col = 0  # root has col 0, min_col represents relative column position
        d = defaultdict(list)
        queue = deque()  # Stores (node, col)
        queue.append((root, 0))
        while queue:
            size = len(queue)
            for _ in range(size):
                curr, col = queue.popleft()
                d[col].append(curr.val)

                # update min_col
                if col < min_col:
                    min_col = col

                if curr.left:
                    queue.append((curr.left, col - 1))
                if curr.right:
                    queue.append((curr.right, col + 1))

        # return result
        result = []
        i = min_col
        while i in d:
            result.append(d[i])
            i += 1
        return result
