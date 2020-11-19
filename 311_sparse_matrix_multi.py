from typing import List
from collections import defaultdict


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Draft 2
        [MEMO] Use dict to store non-zeros, row->[cols] vs. rol->[rows]
        Beats 74%
        """
        I = len(A)
        J = len(A[0])
        K = len(B[0])

        da = defaultdict(list)  # row -> [cols]
        db = defaultdict(list)  # col -> [rows]
        for i in range(I):
            for j in range(J):
                if A[i][j] != 0:
                    da[i].append(j)
        for j in range(J):
            for k in range(K):
                if B[j][k] != 0:
                    db[k].append(j)

        # [MEMO] MUST DO THIS to for 2D array, if you do [[0] * K] * I, each row is a reference to the same array, change one changes all
        ans = [[0] * K for _ in range(I)]
        for i in range(I):
            for k in range(K):
                if i not in da or k not in db:
                    continue

                sum = 0
                for j in da[i]:
                    if j in db[k]:
                        sum += A[i][j] * B[j][k]
                ans[i][k] = sum
        return ans

    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Draft 1
        Solution do not consider sparse, only 16.35%
        """
        I = len(A)
        J = len(A[0])
        K = len(B[0])

        ans = []
        for i in range(I):
            ans.append(list())
            for k in range(K):
                ans[i].append(sum([A[i][x] * B[x][k] for x in range(J)]))
        return ans
