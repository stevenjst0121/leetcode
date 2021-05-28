from typing import List
import heapq
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Remember what is binary heap and how to use heapq
        """
        queue = []
        for num in nums:
            heapq.heappush(queue, num)
            if len(queue) > k:
                heapq.heappop(queue)
        return queue[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.helper(nums, 0, len(nums) - 1, len(nums) - k + 1)

    def quickSelect(self, nums, low, high, ks):
        """Quick Select
        [MEMO] Quick select Algo, very similar to quick sort, but it searches kth smallest in O(N), worst O(N^2)
        Basically you do divide and conquer but only recursively work on one side once partition is done
        """
        # find kth smallest
        # [NOTE] randint, low <= N <= high
        pivot_index = random.randint(low, high)
        pivot = nums[pivot_index]
        # move pivot to end
        nums[pivot_index], nums[high] = nums[high], nums[pivot_index]
        i = low  # the lowest indices where num > pivot
        for j in range(low, high + 1):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]

        # i is pivot now
        if i == ks - 1:
            return nums[i]
        elif i > ks - 1:
            return self.quickSelect(nums, low, i - 1, ks)
        else:
            return self.quickSelect(nums, i + 1, high, ks)
