from typing import List
from math import ceil, log2


class NumArray:
    """
    [MEMO] Segment Tree recursive implementation
    """

    def __init__(self, nums: List[int]):
        # Array implementation
        self.N = len(nums)
        self.H = ceil(log2(self.N))
        self.tree = [0] * (2 * (2 ** self.H) - 1)
        self.buildTree(nums, 0, 0, self.N - 1)

    def buildTree(self, nums, tree_index, lo, hi):
        if lo == hi:
            self.tree[tree_index] = nums[lo]
            return

        mid = lo + (hi - lo) // 2
        self.buildTree(nums, 2 * tree_index + 1, lo, mid)
        self.buildTree(nums, 2 * tree_index + 2, mid + 1, hi)
        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def update(self, index: int, val: int) -> None:
        self.updateUtil(0, 0, self.N - 1, index, val)

    def updateUtil(self, tree_index: int, lo: int, hi: int, index: int, val: int) -> None:
        if lo == hi:
            self.tree[tree_index] = val
            return

        mid = lo + (hi - lo) // 2
        if index > mid:
            self.updateUtil(2 * tree_index + 2, mid + 1, hi, index, val)
        elif index <= mid:
            self.updateUtil(2 * tree_index + 1, lo, mid, index, val)

        self.tree[tree_index] = self.tree[2 * tree_index + 1] + self.tree[2 * tree_index + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeUtil(0, 0, self.N - 1, left, right)

    def sumRangeUtil(self, tree_index: int, lo: int, hi: int, left: int, right: int) -> int:
        if lo > right or hi < left:
            # Completely out of range
            return 0

        if left <= lo and right >= hi:
            # Completely in range
            return self.tree[tree_index]

        mid = lo + (hi - lo) // 2
        if left > mid:
            return self.sumRangeUtil(2 * tree_index + 2, mid + 1, hi, left, right)
        elif right <= mid:
            return self.sumRangeUtil(2 * tree_index + 1, lo, mid, left, right)

        left = self.sumRangeUtil(2 * tree_index + 1, lo, mid, left, mid)
        right = self.sumRangeUtil(2 * tree_index + 2, mid + 1, hi, mid + 1, right)

        return left + right


class NumArray:
    class Node:
        def __init__(self, val: int = 0):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self, nums: List[int]):
        # Tree implementation
        self.N = len(nums)
        self.root = self.buildTree(nums, 0, self.N - 1)

    def buildTree(self, nums, lo, hi):
        if lo == hi:
            return NumArray.Node(nums[lo])

        mid = lo + (hi - lo) // 2
        left = self.buildTree(nums, lo, mid)
        right = self.buildTree(nums, mid + 1, hi)
        node = NumArray.Node(left.val + right.val)
        node.left = left
        node.right = right
        return node

    def update(self, index: int, val: int) -> None:
        self.updateTree(self.root, 0, self.N - 1, index, val)

    def updateTree(self, node, lo, hi, index, val):
        if lo == hi:
            node.val = val
            return

        mid = lo + (hi - lo) // 2
        if mid < index:
            self.updateTree(node.right, mid + 1, hi, index, val)
        else:
            self.updateTree(node.left, lo, mid, index, val)

        node.val = node.left.val + node.right.val

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeTree(self.root, 0, self.N - 1, left, right)

    def sumRangeTree(self, node, lo, hi, left, right):
        if hi < left or right < lo:
            return 0

        if left <= lo and hi <= right:
            return node.val

        mid = lo + (hi - lo) // 2
        if left > mid:
            return self.sumRangeTree(node.right, mid + 1, hi, left, right)
        elif right <= mid:
            return self.sumRangeTree(node.left, lo, mid, left, right)
        else:
            l = self.sumRangeTree(node.left, lo, mid, left, right)
            r = self.sumRangeTree(node.right, mid + 1, hi, left, right)
            return l + r
