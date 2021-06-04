import math
from typing import List
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """Draft 1
        Becareful with handling INF and -INF cases
        Store k as slope in (x, y) pairs, using math.gcd()
        """
        if not points:
            return 0

        max_num = 1
        graph = defaultdict(dict)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x_i, y_i = points[i]
                x_j, y_j = points[j]
                # i
                slope_i = self.getSlope(x_i, y_i, x_j, y_j)
                if slope_i not in graph[(x_i, y_i)]:
                    graph[(x_i, y_i)][slope_i] = 1
                else:
                    graph[(x_i, y_i)][slope_i] += 1
                # j
                slope_j = self.getSlope(x_j, y_j, x_i, y_i)
                if slope_j not in graph[(x_j, y_j)]:
                    graph[(x_j, y_j)][slope_j] = 1
                else:
                    graph[(x_j, y_j)][slope_j] += 1

                max_num = max(
                    max_num, 1 + graph[(x_i, y_i)][slope_i], 1 + graph[(x_j, y_j)][slope_j]
                )
        return max_num

    def getSlope(self, x1, y1, x2, y2):
        delta_x = x1 - x2
        delta_y = y1 - y2
        if delta_x == 0:
            if delta_y > 0:
                return (0, float("Inf"))
            else:
                return (0, float("-Inf"))
        elif delta_y == 0:
            if delta_x > 0:
                return (float("Inf"), 0)
            else:
                return (float("-Inf"), 0)
        else:
            gcd = math.gcd(delta_x, delta_y)
            return (delta_x / gcd, delta_y / gcd)