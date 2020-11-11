from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Solution 1
        [MEMO MEMO] Can simply drop the smaller interval, and use two pointers for iteration
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                result.append([lo, hi])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return result

    # def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    #     """Draft 1
    #     Recursive solution without using any extra space, but only beat 7%
    #     The thing is we actually don't need do truncation, can just drop the smaller interval
    #     """
    #     self.helper(A, B)

    #     return self.result

    # def helper(self, A: List[List[int]], B: List[List[int]]) -> None:
    #     if not A or not B:
    #         return None

    #     # if there no overlap
    #     if A[0][0] > B[0][1]:
    #         self.intervalIntersection(A, B[1:])
    #         return

    #     if B[0][0] > A[0][1]:
    #         self.intervalIntersection(A[1:], B)
    #         return

    #     # Has overlap
    #     self.result.append([max(A[0][0], B[0][0]), min(A[0][1], B[0][1])])

    #     # Continue
    #     if A[0][1] == B[0][1]:
    #         self.intervalIntersection(A[1:], B[1:])
    #     elif A[0][1] < B[0][1]:
    #         self.intervalIntersection(A[1:], B)
    #     else:
    #         self.intervalIntersection(A, B[1:])
