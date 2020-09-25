import pytest
from typing import *
from collections import *


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """"""
        hashes = defaultdict(list)
        for i in range(len(strs)):
            # create tuple of 26 zeros
            l = [0] * 26
            for c in strs[i]:
                l[ord(c) - 97] += 1
            t = tuple(l)

            hashes[t].append(strs[i])

        return hashes.values()


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )
    ],
)
def test_solution(test_input, expected):
    s = Solution()
    result = s.groupAnagrams(test_input)
    assert len(result) == len(expected)
