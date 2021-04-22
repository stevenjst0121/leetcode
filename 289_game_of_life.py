from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Hard part is modify in-place, use value other than 0, 1 to represents previous state
        """
        # -1 means 1 -> 0
        # 2 means 0 -> 1
        offsets = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                status = board[i][j]
                live_count = 0
                neighbors = [(i + offset_i, j + offset_j) for offset_i, offset_j in offsets]
                for n_i, n_j in neighbors:
                    if n_i < 0 or n_i >= M or n_j < 0 or n_j >= N:
                        continue

                    n_status = board[n_i][n_j]
                    if n_status == 1 or n_status == -1:
                        live_count += 1

                if status == 1 and (live_count < 2 or live_count > 3):
                    board[i][j] = -1
                elif status == 0 and live_count == 3:
                    board[i][j] = 2

        for i in range(M):
            for j in range(N):
                status = board[i][j]
                if status == -1:
                    board[i][j] = 0
                elif status == 2:
                    board[i][j] = 1
