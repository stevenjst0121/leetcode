from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Draft 1
        Use heapq, but doesn't use the fact the matrix is sorted

        [TODO] Don't quite understand the solution for binary sort...
        """
        heap = []
        n = len(matrix)
        i, j = 0, 0
        while i < n and j < n:
            val = matrix[i][j]
            heapq.heappush(heap, -1 * val)
            if len(heap) > k:
                heapq.heappop(heap)

            # continue
            if j < n - 1:
                j += 1
            else:
                i += 1
                j = 0

        return -1 * heapq.heappop(heap)