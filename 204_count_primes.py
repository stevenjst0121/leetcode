import pytest
import math
from typing import *
from collections import *


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        flags = [1] * n
        flags[0] = 0
        flags[1] = 0

        prime = 2
        while prime < math.sqrt(n):
            self.crossoff(flags, prime)

            prime = self.get_next_prime(flags, prime)

        return sum(flags)

    def crossoff(self, flags, prime):
        for i in range(prime * prime, len(flags), prime):
            flags[i] = 0

    def get_next_prime(self, flags, prime):
        prime += 1
        while flags[prime] == 0:
            prime += 1
        return prime

    # def countPrimes(self, n: int) -> int:
    #     """
    #     MEMO
    #     ??? Do better
    #     """
    #     if n <= 2:
    #         return 0

    #     counts = [1] * n
    #     counts[0] = 0
    #     counts[1] = 0
    #     for i in range(2, n):
    #         if counts[i] == 0:
    #             continue

    #         j = 2
    #         while i * j < n:
    #             if counts[i * j] > 0:
    #                 counts[i * j] = 0
    #             j += 1
    #     return sum(counts)


@pytest.mark.parametrize(
    "test_input,expected",
    [(10, 4), (0, 0), (1, 0), (2, 0), (3, 1), (499979, 41537)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.countPrimes(test_input) == expected
