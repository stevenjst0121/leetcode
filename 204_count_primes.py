import pytest
from typing import *
from collections import *


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        MEMO
        ??? Do better
        """
        if n <= 2:
            return 0

        counts = [1] * n
        counts[0] = 0
        counts[1] = 0
        for i in range(2, n):
            if counts[i] == 0:
                continue

            j = 2
            while i * j < n:
                if counts[i * j] > 0:
                    counts[i * j] = 0
                j += 1
        return sum(counts)


@pytest.mark.parametrize(
    "test_input,expected",
    [(10, 4), (0, 0), (1, 0), (2, 0), (3, 1), (499979, 41537)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.countPrimes(test_input) == expected
