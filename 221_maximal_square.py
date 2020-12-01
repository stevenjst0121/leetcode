from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Dynamic Programming
        [MEMO] Brilliant way to solve the problem using bottom-up DP
        """
        if not matrix:
            return 0

        M = len(matrix)
        N = len(matrix[0])
        dp = [[0 for _ in range(N)] for _ in range(M)]
        max_dp = 0
        for row in range(M):
            for col in range(N):
                if matrix[row][col] == "0":
                    continue

                if row - 1 < 0 or col - 1 < 0:
                    dp[row][col] = 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1]) + 1
                max_dp = max(max_dp, dp[row][col])
        return max_dp ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """First draft
        Brute force, only beats 5%
        """
        if not matrix:
            return 0

        res = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    continue

                curr_len = 1
                max_len = min(len(matrix) - row, len(matrix[0]) - col)
                while curr_len < max_len and self.checkSquare(matrix, row, col, curr_len + 1):
                    curr_len += 1
                area = curr_len ** 2
                if area > res:
                    res = area
        return res

    def checkSquare(self, matrix: List[List[str]], row: int, col: int, length: int) -> bool:
        # check if sqaure of length exists using [row, col] as top left corner
        i, j = row, col
        while i < row + length and j < col + length:
            if matrix[i][j] == "0":
                return False
            else:
                if j < col + length - 1:
                    j += 1
                else:
                    i += 1
                    j = col
        return True
