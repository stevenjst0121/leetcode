from typing import *
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Max Heap
        Better solution from discussion
        No need to define class with __lt__, just store (key, value) into heap
        """
        heap = []
        for point in points:
            heapq.heappush(heap, (-1 * (point[0] ** 2 + point[1] ** 2), point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [point for _, point in heap]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Solution 1
        Just sort by distance using lambda
        """
        # [NOTE] remember how to sort using lambda
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:K]
