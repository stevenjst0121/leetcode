from collections import defaultdict
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        all_dict = defaultdict(list)
        M = len(matrix)
        N = len(matrix[0])
        for m in range(M):
            for n in range(N):
                all_dict[matrix[m][n]].append((m, n))

        max_path = 0
        dp = [[0] * N for _ in range(M)]
        for num in sorted(all_dict.keys(), key=lambda x: -1 * x):
            positions = all_dict[num]
            for m, n in positions:
                if n == 0 or matrix[m][n - 1] <= matrix[m][n]:
                    left = 1
                else:
                    left = 1 + dp[m][n - 1]
                if n == N - 1 or matrix[m][n + 1] <= matrix[m][n]:
                    right = 1
                else:
                    right = 1 + dp[m][n + 1]
                if m == 0 or matrix[m - 1][n] <= matrix[m][n]:
                    up = 1
                else:
                    up = 1 + dp[m - 1][n]
                if m == M - 1 or matrix[m + 1][n] <= matrix[m][n]:
                    down = 1
                else:
                    down = 1 + dp[m + 1][n]
                dp[m][n] = max(left, right, up, down)
                max_path = max(max_path, dp[m][n])
        return max_path