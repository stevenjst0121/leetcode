from collections import defaultdict
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """Draft 1
        Depth first search, O(M*N), but requires a separate graph
        It is actually possible to directly do DFS on the matrix without using a graph
        And you can also avoid using visited by simply marking visited land 0
        """
        if not grid:
            return 0

        # Construct graph
        graph = defaultdict(list)  # (i, j) -> [(i, j)]
        M = len(grid)
        N = len(grid[0])
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    continue
                # self
                graph[(i, j)].append((i, j))
                # left
                if j > 0 and grid[i][j - 1] == 1:
                    graph[(i, j)].append((i, j - 1))
                # right
                if j < N - 1 and grid[i][j + 1] == 1:
                    graph[(i, j)].append((i, j + 1))
                # up
                if i > 0 and grid[i - 1][j] == 1:
                    graph[(i, j)].append((i - 1, j))
                # down
                if i < M - 1 and grid[i + 1][j] == 1:
                    graph[(i, j)].append((i + 1, j))

        # Traverse to find maximum length
        visited = set()
        max_area = 0
        for root in graph.keys():
            if root in visited:
                continue

            length = 0
            stack = [root]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue

                visited.add(node)
                length += 1
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

            if length > max_area:
                max_area = length

        return max_area
