from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """Stack Solution O(N)
        [MEMO]
        * All bars in stack are in increasing order
        * When get to a point where last bar in stack is larger than current bar, find max area backwards till the bar that is smaller than current bar
        * One trick is to use -1 to indicate left most invisible bar
        """
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        """Divide and Conquer
        O(NLogN), but exceeds time limit for a flat heights O(N^2)
        """
        if not heights:
            return 0

        min_index = 0
        for i in range(len(heights)):
            if heights[i] < heights[min_index]:
                min_index = i
        return max(
            heights[min_index] * len(heights),
            self.largestRectangleArea(heights[:min_index]),
            self.largestRectangleArea(heights[min_index + 1 :]),
        )

    def largestRectangleArea(self, heights: List[int]) -> int:
        """Draft 1
        Bottom-up dp, works but exceeds time limit
        O(N^2)
        """
        N = len(heights)
        # (maximum height can form rectagnle between i and j, area)
        dp = [[(0, 0)] * N for _ in range(N)]

        max_area = -1
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if i == j:
                    height = heights[i]
                    area = heights[i]
                    dp[i][j] = (height, area)
                    if area > max_area:
                        max_area = area
                    continue

                height = min(heights[i], dp[i + 1][j][0])
                area = height * (j - i + 1)
                dp[i][j] = (height, area)
                if area > max_area:
                    max_area = area
        return max_area
