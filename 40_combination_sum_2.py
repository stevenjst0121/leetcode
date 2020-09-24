import pytest
from typing import *
from collections import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Note: Be careful with duplicate results
        Question: What the time complexity???
        """
        candidates.sort()
        return self.combinationSumHelper2(candidates, 0, 0, target)

    def combinationSumHelper2(
        self, candidates: List[int], start: int, presum: int, target: int
    ) -> List[List[int]]:
        if presum > target:
            return []

        results = []
        i = start
        while i < len(candidates):
            sum = presum + candidates[i]
            if sum < target:
                for ll in self.combinationSumHelper2(candidates, i + 1, sum, target):
                    results.append([candidates[i]] + ll)
            elif sum > target:
                break
            else:
                results.append([candidates[i]])

            # increment i and avoid duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            i += 1
        return results


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (
            ([10, 1, 2, 7, 6, 1, 5], 8),
            [
                [1, 1, 6],
                [1, 2, 5],
                [1, 7],
                [2, 6],
            ],
        )
    ],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.combinationSum2(test_input[0], test_input[1]) == expected
