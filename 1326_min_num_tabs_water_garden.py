from typing import List
from collections import defaultdict


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        """Draft 1
        Recursion + memoization, works but exceeds time limit
        """
        self.tap_map = defaultdict(list)
        self.memo = {}

        for i in range(len(ranges)):
            if ranges[i] == 0:
                continue

            left = i - ranges[i]
            right = i + ranges[i]
            for j in range(n + 1):
                if left <= j and right > j:
                    self.tap_map[j].append(i)
        print(self.tap_map)

        opened = set()
        return self.dfs(0, n, ranges, opened)

    def dfs(self, start: int, end: int, ranges: List[int], opened: Set[int]) -> int:
        key = (start, end, tuple(opened))
        if key in self.memo:
            return self.memo[key]

        if start >= end:
            return 0

        min_taps = -1
        avail_taps = self.tap_map[start]
        for i in avail_taps:
            if i in opened:
                continue

            # try to use ith tap
            opened.add(i)
            new_start = i + ranges[i]
            taps_needed = self.dfs(new_start, end, ranges, opened)
            opened.remove(i)
            if taps_needed < 0:
                continue
            else:
                num_taps = 1 + taps_needed
                if min_taps < 0 or num_taps < min_taps:
                    min_taps = num_taps

        self.memo[key] = min_taps
        return min_taps
