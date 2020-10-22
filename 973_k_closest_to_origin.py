from typing import *
import math
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """Max Heap
        Better solution from discussion
        [MEMO] No need to define class with __lt__, just store (key, value) into heap
        """
        heap = []
        for point in points:
            heapq.heappush(heap, (-1 * (point[0] ** 2 + point[1] ** 2), point))
            if len(heap) > K:
                heapq.heappop(heap)
        return [point for _, point in heap]

    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     """Solution 1
    #     Just sort by distance using lambda
    #     """
    #     points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
    #     return points[:K]

    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     """Draft 1
    #     Using max heap
    #     heappush is O(logN), so looping through list and push to queue is O(NlogN), which is no difference then just sort directly
    #     see solution 1
    #     """

    #     class Point:
    #         def __init__(self, loc: List[int] = [0, 0]):
    #             self.loc = loc
    #             # It's a hack for min heap to work as max heap
    #             self.distance = -1 * math.sqrt(self.loc[0] ** 2 + self.loc[1] ** 2)

    #         def __lt__(self, other):
    #             return self.distance < other.distance

    #     stack = []
    #     for point in points:
    #         p = Point(point)
    #         heapq.heappush(stack, p)
    #         if len(stack) > K:
    #             heapq.heappop(stack)
    #     return [p.loc for p in stack]
