from typing import List


class Solution:
    def __init__(self):
        self.offsets = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        """Draft 1
        DFS recursive search, beats 59%
        """
        initial = word[0]
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == initial:
                    visited = set()
                    visited.add((i, j))
                    if self.dfs(board, i, j, visited, word[1:]):
                        return True

        return False

    def dfs(self, board, i, j, visited, word) -> bool:
        if not word:
            return True

        M = len(board)
        N = len(board[0])

        if len(visited) == M * N:
            return False

        initial = word[0]
        for offset in self.offsets:
            new_i = i + offset[0]
            new_j = j + offset[1]
            if new_i < 0 or new_i >= M or new_j < 0 or new_j >= N:
                continue

            if (new_i, new_j) in visited:
                continue

            if board[new_i][new_j] == initial:
                visited.add((new_i, new_j))
                res = self.dfs(board, new_i, new_j, visited, word[1:])
                if res:
                    return True

                visited.remove((new_i, new_j))
        return False
