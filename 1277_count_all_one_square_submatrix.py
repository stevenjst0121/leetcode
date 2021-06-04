from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        num_squares = 0
        for m in range(M):
            for n in range(N):
                if matrix[m][n] == 0:
                    continue

                if m == 0 or n == 0:
                    dp[m][n] = 1
                else:
                    dp[m][n] = 1 + min(dp[m - 1][n], dp[m - 1][n - 1], dp[m][n - 1])
                num_squares += dp[m][n]
        return num_squares