import pytest
from typing import *
from collections import *


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """"""
        d = {}
        for i in range(9):
            for j in range(9):
                # Skip if no number
                if board[i][j] == ".":
                    continue

                num = int(board[i][j])
                # If num does not exit in d
                if d.get(num, None) is None:
                    d[num] = [(i, j)]
                    continue

                # There is num in d, check valid. If valid, add to d

                # Top left of 3x3
                i_s = i - (i % 3)
                j_s = j - (j % 3)

                for (row, col) in d[num]:
                    # Check row and col
                    if row == i or col == j:
                        return False

                    # Check 3x3
                    if row >= i_s and row <= i_s + 2 and col >= j_s and col <= j_s + 2:
                        return False

                # Add to d
                d[num].append((i, j))

        return True


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ),
        (
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            False,
        ),
    ],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.isValidSudoku(test_input) == expected
