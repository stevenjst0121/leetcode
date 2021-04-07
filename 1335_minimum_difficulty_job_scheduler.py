class Solution:
    def __init__(self):
        self.memo = {}

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """Draft 1
        Recursive solution with memo, only beats 5%
        Not sure how a DP solution from bottom-up looks like, but the memo can be improved
        like dp[i][j] represents last cut from i and j days left
        """
        if d <= 0 or len(jobDifficulty) < d:
            return -1

        key = (tuple(jobDifficulty), d)
        if key in self.memo:
            return self.memo[key]

        if d == 1:
            d_best = max(jobDifficulty)
            self.memo[key] = d_best
            # print(f"jobs={jobDifficulty}, d={d}, d_best={d_best}")
            return d_best

        d_best = None
        for i in range(1, len(jobDifficulty) - d + 1 + 1):
            d_rest = self.minDifficulty(jobDifficulty[i:], d - 1)
            if d_rest < 0:
                continue
            d_curr = max(jobDifficulty[:i])
            d_total = d_curr + d_rest
            if not d_best or d_total < d_best:
                d_best = d_total

        assert d_best is not None
        self.memo[key] = d_best
        # print(f"jobs={jobDifficulty}, d={d}, d_best={d_best}")
        return d_best
