from typing import List
from math import ceil, log2


class NumArray:
    """
    [MEMO] Segment Tree recursive implementation
    """

    def __init__(self, nums: List[int]):
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
