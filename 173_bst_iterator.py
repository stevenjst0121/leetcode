# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.curr = root
        self.stack = deque()

    def next(self) -> int:
        """
        @return the next smallest number
        Time is O(N)
        Space is O(K) where K is maximum height
        """
        while self.curr or self.stack:
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
                continue

            self.curr = self.stack.pop()
            result = self.curr.val
            self.curr = self.curr.right
            return result

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curr or self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()