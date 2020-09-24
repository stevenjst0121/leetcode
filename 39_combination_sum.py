import pytest
from typing import *
from collections import *


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Note: Be careful with duplicate results
        Question: What the time complexity???
        """
        candidates.sort()
        return self.combinationSumHelper(candidates, 0, 0, target)

    def combinationSumHelper(
        self, candidates: List[int], start: int, presum: int, target: int
    ) -> List[List[int]]:
        # Start represents the last (biggest) elemented added in previous iteration
        if presum > target:
            return []

        results = []
        for i in range(start, len(candidates)):
            sum = presum + candidates[i]
            if sum < target:
                for ll in self.combinationSumHelper(candidates, i, sum, target):
                    results.append([candidates[i]] + ll)
            elif sum > target:
                break
            else:
                results.append([candidates[i]])
        return results


@pytest.mark.parametrize(
    "test_input,expected",
    [(([2, 3, 6, 7], 7), [[2, 2, 3], [7]]), (([2, 3, 5], 8), [[2, 2, 2, 2], [2, 3, 3], [3, 5]])],
)
def test_solution(test_input, expected):
    s = Solution()
    assert s.combinationSum(test_input[0], test_input[1]) == expected
