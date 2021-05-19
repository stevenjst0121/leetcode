from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """Solution Stack
        [MEMO] In 84 we solved maximum rectangle in histogram using stack
        Here we simply build histogram row by row. And for each row, we apply
        solution in 84) to calculate max area.
        """
        if not matrix:
            return 0

        dp = [0] * len(matrix[0])
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    dp[j] = 0
                else:
                    dp[j] += 1

            max_area = max(max_area, self.helper(dp))
        return max_area

    def helper(self, dp):
        stack = [-1]
        max_area = 0
        for i in range(len(dp)):
            while stack[-1] != -1 and dp[stack[-1]] >= dp[i]:
                curr_height = dp[stack.pop()]
                curr_width = i - stack[-1] - 1
                max_area = max(max_area, curr_height * curr_width)
            stack.append(i)

        while stack[-1] != -1:
            curr_height = dp[stack.pop()]
            curr_width = len(dp) - stack[-1] - 1
            max_area = max(max_area, curr_height * curr_width)
        return max_area

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """Solution DP
        [MEMO] Calculate maximum width at each given point, and then move up the column to calculate max area
        """
        max_area = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0":
                    continue

                if j > 0:
                    width = dp[i][j - 1] + 1
                else:
                    width = 1
                dp[i][j] = width

                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width * (i - k + 1))
        return max_area
