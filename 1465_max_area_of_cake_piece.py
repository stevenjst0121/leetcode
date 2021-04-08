from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        max_height = -1
        for i in range(1, len(horizontalCuts)):
            height = horizontalCuts[i] - horizontalCuts[i - 1]
            if height > max_height:
                max_height = height

        verticalCuts.sort()
        verticalCuts = [0] + verticalCuts + [w]
        max_width = -1
        for j in range(1, len(verticalCuts)):
            width = verticalCuts[j] - verticalCuts[j - 1]
            if width > max_width:
                max_width = width

        return (max_height * max_width) % (10 ** 9 + 7)
