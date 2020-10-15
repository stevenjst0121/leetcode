from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [MEMO] Remember what is binary heap and how to use heapq
        """
        queue = []
        for num in nums:
            heapq.heappush(queue, num)
            if len(queue) > k:
                heapq.heappop(queue)
        return queue[0]