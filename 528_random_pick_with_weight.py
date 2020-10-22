from typing import *
from random import randrange, random


class Solution:
    # TODO Think O(1) lookup solution

    def __init__(self, w: List[int]):
        self.w = w
        self.w_accumulate = []
        pre_sum = 0
        for val in w:
            pre_sum = val + pre_sum
            self.w_accumulate.append(pre_sum)
        self.total = pre_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        # run a binary search to find the target zone
        """[MEMO] Easiest way to write binary search without recursion"""
        low, high = 0, len(self.w_accumulate) - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.w_accumulate[mid]:
                low = mid + 1
            else:
                high = mid
        return low

    # def pickIndex(self) -> int:
    #     """Draft 1
    #     Using accumulate sum and randrange(), problem is lookup with rand is not O(1), only got to 34% when optimized with divide and conqur
    #     """
    #     return self.helper(randrange(1, self.total + 1, 1), 0, len(self.w_accumulate) - 1)

    # def helper(self, target: int, start: int, end: int) -> int:
    #     if start == end:
    #         return start

    #     mid = int((start + end) / 2)
    #     if mid == start:
    #         if target <= self.w_accumulate[mid]:
    #             return mid
    #         return self.helper(target, mid + 1, end)

    #     if target > self.w_accumulate[mid - 1] and target <= self.w_accumulate[mid]:
    #         return mid

    #     if target > self.w_accumulate[mid]:
    #         return self.helper(target, mid + 1, end)
    #     else:
    #         return self.helper(target, start, mid - 1)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()