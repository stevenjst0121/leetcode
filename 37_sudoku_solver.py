import pytest
from typing import *
from collections import *


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """"""
        exists = {}
        first_loc = None
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    if first_loc is None:
                        first_loc = (i, j)
                    continue

                num = int(board[i][j])
                if exists.get(num, None) is None:
                    exists[num] = [(i, j)]
                else:
                    exists[num].append((i, j))

        self.solveSudokuHelper(board, first_loc[0], first_loc[1], exists)

    def solveSudokuHelper(self, board: List[List[str]], i: int, j: int, exists: Dict) -> bool:
        for num in range(1, 10):
            if not self.isValid(num, i, j, exists):
                continue

            # Try num
            board[i][j] = str(num)
            if exists.get(num, None) is None:
                exists[num] = [(i, j)]
            else:
                exists[num].append((i, j))

            # Continue, find next to try
            ii = i
            jj = j
            while board[ii][jj] != ".":
                if jj < 8:
                    jj += 1
                elif ii < 8:
                    ii += 1
                    jj = 0
                else:
                    # This means done!
                    return True

            # Try
            if self.solveSudokuHelper(board, ii, jj, exists):
                return True

            # Try was not good, revert and continue
            board[i][j] = "."
            exists[num].remove((i, j))

        return False

    def isValid(self, num: int, i: int, j: int, exists: Dict) -> bool:
        if exists.get(num, None) is None:
            return True

        i_s = i - (i % 3)
        j_s = j - (j % 3)
        for (row, col) in exists[num]:
            if row == i or col == j:
                return False

            if row >= i_s and row <= i_s + 2 and col >= j_s and col <= j_s + 2:
                return False
        return True


@pytest.mark.parametrize(
    "test_input,expected",
    [],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.solveSudoku(test_input) == expected
