from typing import List


class Solution:
    # TODO Look at other solutions
    def numIslands(self, grid: List[List[str]]) -> int:
        """Draft 1
        Recursive search, very similar logic to DFS treating the grid as an undirected graph
        """
        m = len(grid)
        n = len(grid[0])

        result = 0
        i, j = 0, 0
        while i < m:
            loc = grid[i][j]
            # loc is land
            if loc == "1":
                self.mark_island(i, j, grid)
                result += 1

            # continue
            if j < n - 1:
                j += 1
            else:
                i += 1
                j = 0
        return result

    def mark_island(self, i: int, j: int, grid: List[List[str]]) -> None:
        if grid[i][j] in ("0", "2"):
            # already marked or water
            return

        # mark island
        grid[i][j] = "2"

        # mark surroundings
        if i > 0:
            self.mark_island(i - 1, j, grid)
        if i < len(grid) - 1:
            self.mark_island(i + 1, j, grid)
        if j > 0:
            self.mark_island(i, j - 1, grid)
        if j < len(grid[0]) - 1:
            self.mark_island(i, j + 1, grid)
