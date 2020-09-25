import pytest
from typing import *
from collections import *


class Solution:
    def isHappy(self, n: int) -> bool:
        """"""
        s = set()
        s.add(n)
        while True:
            print(n)
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            n = sum

            if n == 1:
                return True

            if n in s:
                return False

            s.add(n)


@pytest.mark.parametrize(
    "test_input,expected",
    [(19, True), (2, False)],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.isHappy(test_input) == expected
