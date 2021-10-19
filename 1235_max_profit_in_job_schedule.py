import bisect
from typing import *


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        [MEMO]
        Simple backtrack (bruteforce) solution will timeout
        The problem has optimal substructure, so DP must can be used!!!
        """
        schedules = []
        for i in range(len(startTime)):
            bisect.insort(schedules, (startTime[i], endTime[i], profit[i]))

        dp = [0] * (len(schedules) + 1)
        for i in range(len(schedules) - 1, -1, -1):
            # Do the job at i
            profit = schedules[i][2]
            profit_do = profit
            next_index = self.findNextIndex(schedules, schedules[i][1])
            if next_index < len(schedules):
                profit_do += dp[next_index]

            # Do not do the job at i
            profit_not_do = dp[i + 1]

            # Combine
            dp[i] = max(profit_do, profit_not_do)

        return dp[0]

    def findNextIndex(self, schedules, threshold):
        fake_schedule = (threshold, threshold, 0)
        return bisect.bisect_left(schedules, fake_schedule)