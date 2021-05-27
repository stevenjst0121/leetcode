from typing import List
from collections import deque


class Solution:
    def trap(self, height: List[int]) -> int:
        """Solution DP
        [MEMO+1] brilliant solution using DP by storing max from both sides
        """
        if not height:
            return 0

        N = len(height)
        max_left = [0] * N
        max_so_far = float("-Inf")
        for i in range(N):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_left[i] = max_so_far

        max_right = [0] * N
        max_so_far = float("-Inf")
        for i in range(N - 1, -1, -1):
            if height[i] > max_so_far:
                max_so_far = height[i]
            max_right[i] = max_so_far

        result = 0
        for i in range(N):
            result += min(max_left[i], max_right[i]) - height[i]
        return result

    def trap(self, height: List[int]) -> int:
        """Solution Two Pointer
        [MEMO+1] Use the concept of Solution DP that only once side max matters
        Same O(n), but just reduces the number of iterations
        """
        if not height:
            return 0

        ans = 0
        left = 0
        right = len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans

    def trap(self, height: List[int]) -> int:
        """Stack solution
        It's gonna be hard to think of it...
        Similar to Solution DP but only loop through once
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

    # def trap(self, height: List[int]) -> int:
    #     """Draft 1
    #     Form a filled_height list
    #     For each column, find the biggest prev column and then fill the middle
    #     Subtract two to get answer. Worst case seems O(n^2)?
    #     """
    #     filled_height = height.copy()
    #     for curr, h in enumerate(height):
    #         prev = curr - 1
    #         biggest_prev = -1
    #         while prev >= 0:
    #             prev_h = height[prev]
    #             if prev_h >= h:
    #                 biggest_prev = prev
    #                 break

    #             if biggest_prev < 0 or prev_h > height[biggest_prev]:
    #                 biggest_prev = prev
    #             prev -= 1

    #         if biggest_prev >= 0:
    #             fill_level = min(h, height[biggest_prev])
    #             for i in range(biggest_prev + 1, curr):
    #                 if filled_height[i] < fill_level:
    #                     filled_height[i] = fill_level

    #     return sum(filled_height) - sum(height)
