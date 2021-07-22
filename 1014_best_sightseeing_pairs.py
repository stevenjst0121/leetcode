from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        [MEMO] First realize the problem is to find max(values[i] + i) and max(values[j] - j)
        Then do dp twice from both sides for i and j
        """
        N = len(values)

        dp_j = [0] * N
        max_j = float("-Inf")
        for j in range(N - 1, -1, -1):
            max_j = max(max_j, values[j] - (j))
            dp_j[j] = max_j

        max_score = float("-Inf")
        for i in range(0, N - 1):
            score = values[i] + i + dp_j[i + 1]
            max_score = max(max_score, score)
        return max_score