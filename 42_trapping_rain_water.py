from typing import List
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        """Stack solution
        [MEMO] It's gonna be hard to think of it...
        """
        ans = 0
        curr = 0
        size = len(height)
        stack = deque()
        while curr < size:
            while stack and height[curr] > height[stack[0]]:
                top = stack.popleft()
                if not stack:
                    break
                distance = curr - stack[0] - 1
                bounded_height = min(height[curr], height[stack[0]]) - height[top]
                ans += distance * bounded_height
            stack.appendleft(curr)
            curr += 1

        return ans

    def trap(self, height: List[int]) -> int:
        """Solution DP
        [MEMO] brilliant solution using DP by storing max from both sides
        """
        if not height:
            return 0

        size = len(height)
        ans = 0
        left_max = [0] * size
        for i, h in enumerate(height):
            if i == 0:
                left_max[i] = h

            left_max[i] = max(h, left_max[i - 1])

        right_max = [0] * size
        right_max[size - 1] = height[-1]
        for j in range(size - 2, -1, -1):
            right_max[j] = max(height[j], right_max[j + 1])

        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        return ans

    def trap(self, height: List[int]) -> int:
        """Draft 1
        Form a filled_height list
        For each column, find the biggest prev column and then fill the middle
        Subtract two to get answer. Worst case seems O(n^2)?
        """
        filled_height = height.copy()
        for curr, h in enumerate(height):
            prev = curr - 1
            biggest_prev = -1
            while prev >= 0:
                prev_h = height[prev]
                if prev_h >= h:
                    biggest_prev = prev
                    break

                if biggest_prev < 0 or prev_h > height[biggest_prev]:
                    biggest_prev = prev
                prev -= 1

            if biggest_prev >= 0:
                fill_level = min(h, height[biggest_prev])
                for i in range(biggest_prev + 1, curr):
                    if filled_height[i] < fill_level:
                        filled_height[i] = fill_level

        return sum(filled_height) - sum(height)
